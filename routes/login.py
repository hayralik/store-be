from flask import request
from flask_jwt_extended import create_access_token
from datetime import timedelta

def setup_login(app, User, bcrypt):

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Создаём токен
            access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401
    