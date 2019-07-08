from flask import Flask, request, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import config

def best_offer_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/api/search')
    def search():
        ml = urlopen(config.get_ml_url_for(request.args.get('q', '')))
        amzn = urlopen(config.get_amazon_url_for(request.args.get('q', '')))
        ml_html = BeautifulSoup(ml, 'html.parser')
        amzn_html = BeautifulSoup(amzn, 'html.parser')
        results = gather_results(ml_html, amzn_html)

        return jsonify({"results": results, "status_code": 200})
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return jsonify({"results": "not found", "status_code": 404})

    return app


def get_products(html, page):
    items = []
    if page == 'ml':
        product_list = html.find('ol', id="searchResults")
        if product_list:
            for item in product_list.find_all('li', class_="results-item"):
                items.append(str(item))
    if page == 'amzn':
        product_list = html.find('div', class_="s-result-list")
        if product_list:
            for item in product_list.find_all('div', attrs={'data-asin': True}):
                items.append(str(item))
    return items

def gather_results(ml, amzn):
    return [get_products(ml, 'ml'), get_products(amzn, 'amzn')]
