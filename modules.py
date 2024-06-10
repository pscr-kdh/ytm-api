from ytmusicapi import YTMusic

    # Singleton for YTMusic
def get_ytmusic():
    if not hasattr(get_ytmusic, 'ytmusic'):
        get_ytmusic.ytmusic = YTMusic("oauth.json")  # Initialize YTMusic once
    return get_ytmusic.ytmusic

# thumbnails array를 받아 가장 해상도가 큰 것을 뽑고 artwork dictonary풍으로 바꿈
def coverart_to_artwork(item):
    cover_art_for_new_data = {}
    cover_art_max = max(item['thumbnails'], key=lambda x: x['width']) if item['thumbnails'] else None
    if cover_art_max != None:
        cover_art_for_new_data = {
            "url": cover_art_max['url'],
            "width": cover_art_max['width'],
            "height": cover_art_max['height']
        }
    return cover_art_for_new_data

def thumbnails_to_image_url(thumbnails_list):
    return max(thumbnails_list, key=lambda x: x['width'])['url'] if thumbnails_list else None