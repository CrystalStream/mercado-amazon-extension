from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import config
import best_offer

"""Create and configure an instance of the Flask application."""
app = Flask(__name__)

@app.route('/api/search')
def search():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    query = request.args.get('q', '')
    ml = requests.get(config.get_ml_url_for(query), headers=headers)
    amzn = requests.get(config.get_amazon_url_for(query), headers=headers)
    ml_html = BeautifulSoup(ml.text, 'html.parser')
    amzn_html = BeautifulSoup(amzn.text, 'html.parser')
    results = best_offer.gather_results(ml_html, amzn_html)

    return jsonify({"results": results, "status_code": 200})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"results": "not found", "status_code": 404})



if __name__ == '__main__':
    best_offer_app()
