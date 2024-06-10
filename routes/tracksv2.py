from flask import Blueprint, request, jsonify
from services.track_service import (
    get_track_details_v2,
)
from auth import require_api_key
from modules import get_ytmusic

tracks_v2_bp = Blueprint('tracks_v2', __name__, url_prefix='/v2/tracks')

@tracks_v2_bp.route('/details', methods=['GET'])
@require_api_key
def track_details_endpoint():
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_track_details_v2(ytm, track_id)
    return jsonify(result)