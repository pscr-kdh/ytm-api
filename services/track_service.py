from modules import coverart_to_artwork
import re, yt_dlp, os

def get_track_details(ytm, track_id):
    data = ytm.get_watch_playlist(track_id)
    thumbnails = data['tracks'][0]['thumbnail']
    coverart = max(thumbnails, key=lambda x: x['width']) if thumbnails else None
    
    artists = []
    for art in data['tracks'][0]['artists']:
        tmp = {"alias": art['name'], "id": art['id'], "adamid": art['id']}
        artists.append(tmp)


    dtr = {
        "layout": "5",
        "type": "MUSIC",
        "key": track_id,
        "title": data['tracks'][0]['title'],
        "subtitle": data['tracks'][0]['artists'][0]['name'],
        "genres": {"primary": data['tracks'][0]['album']['name']}, # 장르는 지원되지 않으므로 stub로 대충 앨범명을 반환
        "images": {"coverart": coverart['url'], "coverarthq": coverart['url']},
        "artists": artists,
        "trackadamid": track_id
    }

    return dtr

def get_track_details_v2(ytm, track_id):
    # partial implementation: 가사 불러오는데만 쓰므로
    if track_id == 'undefined':
        return {}
    data = ytm.get_watch_playlist(track_id)
    lyrics = ytm.get_lyrics(data['lyrics'])
    lyrics_split = re.split('\r\n|\n', lyrics['lyrics'])
    return {
        "resources": {
            "lyrics": {
                data['lyrics']: {
                    "id": data['lyrics'],
                    "href": "https://unsupported.shazam.com",
                    "type": "lyrics",
                    "attributes": {
                        "text": lyrics_split
                    }
                }
            }
        }
    }


def get_youtube_video(ytm, name, track_id):
    return {
        "actions":[ 
            {
                "uri": "https://youtu.be/" + track_id
            }
        ]
    }

def get_similar_tracks(ytm, track_id):
    # Implement the logic to get similar tracks
    return {"track_id": track_id, "similar_tracks": []}

def get_total_shazams(ytm, track_id):
    # Implement the logic to get total shazams
    return {"track_id": track_id, "total_shazams": 0}

def recognize_track(ytm, file):
    # Implement the logic to recognize track from binary file
    return {"recognized_track": {}}

def get_related_tracks(ytm, track_id):
    data = ytm.get_watch_playlist(track_id)
    related_id = data['related']
    data = ytm.get_song_related(related_id)
    dtr = []
    for item in data[0]['contents']:
        
        thumbnails = item['thumbnails']
        coverart = max(thumbnails, key=lambda x: x['width']) if thumbnails else None
    
        data = {
            "layout": "5",
            "type": "MUSIC",
            "key": item['videoId'],
            "title": item['title'],
            "subtitle": item['artists'][0]['name'],
            "images": {
                "coverart": coverart['url'],
                "covearthq": coverart['url']
            }
        }
        dtr.append(data)

    return dtr

def download_youtube_mp3(track_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'/tmp/{track_id}.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f'https://youtu.be/{track_id}', download=True)
        filename = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
    
    if not os.path.exists(filename):
        raise FileNotFoundError("MP3 file not found after download")

    return filename