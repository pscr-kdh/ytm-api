from flask import Blueprint, request, jsonify
from modules import get_ytmusic
from auth import require_api_key
from services.chart_service import (
    get_city_charts,
    get_world_charts,
    get_genre_world_charts,
    get_country_charts,
    get_genre_country_charts
)

charts_bp = Blueprint('charts', __name__, url_prefix='/v1/charts')

@charts_bp.route('/city', methods=['GET'])
@require_api_key
def city_charts_endpoint():
    city_id = request.args.get('city_id')
    country_code = request.args.get('country_code')
    result = get_city_charts(city_id, country_code)
    return jsonify(result)

@charts_bp.route('/world', methods=['GET'])
@require_api_key
def world_charts_endpoint():
    ytmusic = get_ytmusic()
    country_code = request.args.get('country_code')
    result = get_world_charts(ytmusic, country_code)
    return jsonify(result)

@charts_bp.route('/genre-world', methods=['GET'])
@require_api_key
def genre_world_charts_endpoint():
    genre_code = request.args.get('genre_code')
    country_code = request.args.get('country_code')
    result = get_genre_world_charts(genre_code, country_code)
    return jsonify(result)

@charts_bp.route('/country', methods=['GET'])
@require_api_key
def country_charts_endpoint():
    country_code = request.args.get('country_code')
    ytmusic = get_ytmusic()
    result = get_country_charts(ytmusic, country_code)
    dtr = jsonify(result)
    dtr.headers.add("Access-Control-Allow-Origin", "*")
    return dtr

@charts_bp.route('/genre-country', methods=['GET'])
@require_api_key
def genre_country_charts_endpoint():
    genre_code = request.args.get('genre_code')
    country_code = request.args.get('country_code')
    result = get_genre_country_charts(genre_code, country_code)
    return jsonify(result)
