from flask import Flask, request, jsonify

def best_offer_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/api/search')
    def search():
        import pdb; pdb.set_trace()
        return jsonify({"status": "200"})
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return jsonify({"data": "404 not found"})


    return app
