from flask import Flask
from routes.search import search_bp
from routes.artists import artists_bp
from routes.tracks import tracks_bp
from routes.charts import charts_bp
from routes.tracksv2 import tracks_v2_bp
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

app.register_blueprint(search_bp)
app.register_blueprint(artists_bp)
app.register_blueprint(tracks_bp)
app.register_blueprint(charts_bp)
app.register_blueprint(tracks_v2_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
