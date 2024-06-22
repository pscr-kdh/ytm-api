from modules import thumbnails_to_image_url
def search_multi(ytmusic, query, search_type):
    type = None
    if search_type == "SONGS":
        type = "songs"
    elif search_type == "ARTISTS":
        type = "artists"

    data = ytmusic.search(query, filter=type)
    dtr = {"tracks": {"hits": []}, 'artists': {"hits": []}}
    for d in data:

        if d['resultType'] == 'song':
            track = {'layout': '5', 'type': 'MUSIC', 'key': d['videoId'], 'title': d['title']}
            
            imgurl = thumbnails_to_image_url(d['thumbnails'])
            track['images'] = {'coverart': imgurl, 'coverarthq': imgurl}
            track['hub'] = {'actions': [{}, {'name': 'youtube', 'type': 'uri', 'uri': os.environ.get('DOMAIN_NAME') + 'v1/tracks/download?track_id=' + d['videoId']}]}
            track['artists'] = d['artists']
            for i in range(len(track['artists'])):
                track['artists'][i]['adamid'] = track['artists'][i]['id']
            if len(track['artists']) == 0:
                track['artists'].append({'adamid': None, 'id': None, 'name': 'Various Artists'})
            track['url'] = 'https://youtu.be/' + d['videoId']
            
            dtr['tracks']['hits'].append({"track": track})
   
        elif d['resultType'] == 'artist':
            print(d)
            artist = {'avatar': thumbnails_to_image_url(d['thumbnails']),
                      'verified': False}
            # artists 배열이 있는 경우
            if 'artists' in d:
                artist['name'] = d['artists'][0]['name']
                artist['weburl'] = 'https://music.youtube.com/channel/' + d['artists'][0]['id']
                artist['adamid'] = d['artists'][0]['id']

            # artist string이 있는 경우
            elif 'artist' in d:
                artist['name'] = d['artist']
                artist['weburl'] = 'https://music.youtube.com/channel/' + d['browseId'],
                artist['adamid'] = d['browseId']

            dtr['artists']['hits'].append({"artist": artist})

        else:
            continue

    return dtr

def search_suggest(ytmusic, query):
    res = ytmusic.get_search_suggestions(query);
    hints = []
    for r in res:
        hints.append({"term": r}.copy())
    return {"hints": hints}
