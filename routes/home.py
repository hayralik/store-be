from flask import jsonify

def setup_home(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Hello from Flask!"})
