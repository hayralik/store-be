from flask import jsonify

def setup_home(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Ура! Hello from Flask!"})
