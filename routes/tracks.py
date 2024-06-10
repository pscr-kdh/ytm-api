from flask import Blueprint, request, jsonify, send_file
import os
import re
from auth import require_api_key

from services.track_service import (
    get_track_details,
    get_youtube_video,
    get_similar_tracks,
    get_total_shazams,
    recognize_track,
    get_related_tracks,
    download_youtube_mp3
)
from modules import get_ytmusic

tracks_bp = Blueprint('tracks', __name__, url_prefix='/v1/tracks')

@tracks_bp.route('/details', methods=['GET'])
@require_api_key
def track_details_endpoint():
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_track_details(ytm, track_id)
    return jsonify(result)

@tracks_bp.route('/youtube-video', methods=['GET'])
@require_api_key
def youtube_video_endpoint():
    name = request.args.get('name')
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_youtube_video(ytm, name, track_id)
    return jsonify(result)

@tracks_bp.route('/similarities', methods=['GET'])
@require_api_key
def track_similarities_endpoint():
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_similar_tracks(ytm, track_id)
    return jsonify(result)

@tracks_bp.route('/total-shazams', methods=['GET'])
@require_api_key
def total_shazams_endpoint():
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_total_shazams(ytm, track_id)
    return jsonify(result)

@tracks_bp.route('/recognize', methods=['POST'])
@require_api_key
def recognize_track_endpoint():
    file = request.files['input']
    ytm = get_ytmusic()
    result = recognize_track(ytm, file)
    return jsonify(result)

@tracks_bp.route('/related', methods=['GET'])
@require_api_key
def related_tracks_endpoint():
    track_id = request.args.get('track_id')
    ytm = get_ytmusic()
    result = get_related_tracks(ytm, track_id)
    return jsonify(result)

@tracks_bp.route('/download', methods=['GET'])
@require_api_key
def download():
    track_id = request.args.get('track_id')
    if not track_id:
        return jsonify({"error": "track_id is required"}), 400
    
    if re.match(r'^[a-zA-Z0-9_-]{11}$', track_id) is None:
        return jsonify({"error": "Not a valid YouTube track_id type"}), 400

    try:
        mp3_path = download_youtube_mp3(track_id)
        return send_file(mp3_path, as_attachment=True, mimetype='audio/mp3')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(mp3_path):
            os.remove(mp3_path)