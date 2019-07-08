from flask import Flask, request, jsonify
from urllib.request import urlopen
import config

def best_offer_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/api/search')
    def search():
        ml_html = urlopen(config.get_ml_url_for(request.args.get('q', '')))
        am_html = urlopen(config.get_amazon_url_for(request.args.get('q', '')))
        return jsonify({"results": [ml_html.results, am_html.results], "status_code": 200})
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return jsonify({"results": "not found", "status_code": 404})

    return app
