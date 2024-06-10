from flask import request, jsonify
from functools import wraps
import os

def require_api_key(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-rapidapi-key')
        if api_key and api_key == os.environ['x-rapidapi-key']:
            return func(*args, **kwargs)
        else:
            response = jsonify({'error': 'Forbidden', 'message': 'Invalid or missing API key'})
            response.status_code = 403
            return response
    return decorated_function