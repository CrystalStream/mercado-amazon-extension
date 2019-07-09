from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import config
import utils

"""Create and configure an instance of the Flask application."""
app = Flask(__name__)

@app.route('/api/search')
def search():
    ml = requests.get(config.get_ml_url_for(request.args.get('q', '')))
    amzn = requests.get(config.get_amazon_url_for(request.args.get('q', '')))
    ml_html = BeautifulSoup(ml.text, 'html.parser')
    amzn_html = BeautifulSoup(amzn.text, 'html.parser')
    results = utils.gather_results(ml_html, amzn_html)

    return jsonify({"results": results, "status_code": 200})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"results": "not found", "status_code": 404})



if __name__ == '__main__':
    best_offer_app()
