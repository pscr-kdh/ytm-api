import os
from modules import coverart_to_artwork

def get_artist_details(ytmusic, artist_id):
    data = ytmusic.get_artist(artist_id)
    new_data = convert_chart_format(data)
    return {"data": [new_data]}

# ytmusic artist 목록 반환값을 구 API artist 목록 반환값 비슷하게 바꿈
def convert_chart_format(data):
    artist_id = data['channelId']
    artist_name = data['name']
    views = data['views']
    cover_art_for_new_data = coverart_to_artwork(data)
    description = data['description']
    
    top_songs_data = []
    for item in data['songs']['results']:
        new_item = {
            "id": item['videoId'],
            "type": "songs",
            "href": "/v1/catalog/us/songs/" + item['videoId'],
            "attributes": {
                "artwork": coverart_to_artwork(item),
                "name": item['title'],
                "artistName": item['artists'][0]['name'],
                "albumName": item['album']['name'],
                "albumId": item['album']['id'],
                "isAvailable": item['isAvailable'],
                "previews": [{"url": os.environ.get('DOMAIN_NAME') + 'v1/tracks/download?track_id=' + item['videoId']}]
            }
        }
        top_songs_data.append(new_item)

    new_data = {
        "id": artist_id,
        "attributes": {"genreNames": [views], #genre를 얻어올 수 없으므로 대신 views를 반환하기로 함
                        "artwork": cover_art_for_new_data,
                        "artistBio": description,
                        "name": artist_name,
                        },
        "views": {"top-songs": {"data": top_songs_data}}
    }
    
    return new_data
