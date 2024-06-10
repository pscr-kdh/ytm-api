from flask import Blueprint, request, jsonify
from services.search_service import search_multi, search_suggest
from auth import require_api_key
from modules import get_ytmusic

search_bp = Blueprint('search', __name__, url_prefix='/v1/search')

@search_bp.route('/multi', methods=['GET'])
@require_api_key
def search_multi_endpoint():
    ytmusic = get_ytmusic()
    query = request.args.get('query')
    search_type = request.args.get('search_type')
    result = search_multi(ytmusic, query, search_type)
    return jsonify(result)

@search_bp.route('/suggest', methods=['GET'])
@require_api_key
def search_suggest_endpoint():
    ytmusic = get_ytmusic()
    query = request.args.get('query')
    result = search_suggest(ytmusic, query)
    return jsonify(result)
