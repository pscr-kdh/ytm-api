import re

def get_city_charts(city_id, country_code):
    # stub
    return {"city_id": city_id, "country_code": country_code, "charts": []}

def get_world_charts(ytmusic, country_code):
    chart = ytmusic.get_charts()
    dtr = convert_chart_format(chart['songs']['items'])
    return dtr

def get_genre_world_charts(genre_code, country_code):
    # stub
    return {"genre_code": genre_code, "country_code": country_code, "charts": []}

def get_country_charts(ytmusic, country_code):
    if re.match(r'^[A-Z]{2}$', country_code) == False:
        return {}
    
    chart = ytmusic.get_charts(country_code)
    dtr = convert_chart_format(chart['songs']['items'])
    return dtr

def get_genre_country_charts(genre_code, country_code):
    # stub
    return {"genre_code": genre_code, "country_code": country_code, "charts": []}

# ytmusic 차트 목록 반환값을 구 API 차트 목록 반환값 비슷하게 바꿈
def convert_chart_format(data):
    
    new_format = []
    for item in data:
        video_id = item['videoId']
        artist_name = item['artists'][0]['name'] if item['artists'] else 'Unknown Artist'
        artist_id = item['artists'][0]['id'] if item['artists'] else None
        title = item['title']

        cover_art_url = max(item['thumbnails'], key=lambda x: x['width'])['url'] if item['thumbnails'] else None

        new_item = {
            "id": video_id,
            "key": video_id,
            "type": "songs",
            "title": title,
            "href": f"/watch?v={video_id}",
            "subtitle": artist_name,
            "artists": [{"adamid": artist_id}] if artist_id else [],
            "images": {"coverart": cover_art_url} if cover_art_url else {}
        }
        new_format.append(new_item)

    return new_format