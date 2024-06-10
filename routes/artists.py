from flask import Blueprint, request, jsonify
from services.artist_service import get_artist_details
from auth import require_api_key
from modules import get_ytmusic

artists_bp = Blueprint('artists', __name__, url_prefix='/v2/artists')

@artists_bp.route('/details', methods=['GET'])
@require_api_key
def artist_details_endpoint():
    artist_id = request.args.get('artist_id')
    ytmusic = get_ytmusic()
    result = get_artist_details(ytmusic, artist_id)
    return jsonify(result)
