from flask import Flask, jsonify, request
from flask_cors import CORS  # добавьте этот импорт
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'ваш-секретный-ключ-123'  # поменяйте на свой

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'

# Временное хранилище (потом заменим на БД)
users_db = []

@app.route('/api/register', methods=['POST'])
def register():
    print("Полученные данные:", request.get_json())
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Проверка на существующего пользователя
    for user in users_db:
        if user['email'] == email:
            return {'message': 'User already exists'}, 400

    if len(password) < 6:
        return {'message': 'The password must contain at least 6 characters!'}, 400

    # Хешируем пароль
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Сохраняем пользователя
    new_user = {
        'id': len(users_db) + 1,
        'email': email,
        'password': hashed_password
    }
    users_db.append(new_user)

    return {'message': 'User created successfully'}, 201


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Ищем пользователя в users_db
    for user in users_db:
        if user['email'] == email and bcrypt.check_password_hash(user['password'], password):
            # Создаём токен
            access_token = create_access_token(identity=str(user['id']), expires_delta=timedelta(days=1))
            return {'access_token': access_token}, 200

    return {'message': 'Invalid credentials'}, 401


@app.route('/api/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = int(get_jwt_identity())
    
    # Ищем пользователя по id
    for user in users_db:
        if user['id'] == current_user_id:
            return {'id': user['id'], 'email': user['email']}, 200
    
    return {'message': 'User not found'}, 404


@app.route('/api/users')
def users():
    header = ("X-Secret-Key", "mysecret")
    if header not in request.headers.items():
        return {'message': '|Forbidden'}, 403
    return jsonify([{'id': user['id'], 'email': user['email']} for user in users_db])


@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/api/products')
def products():
    products_list = [
        {"id": 1, "name": "Ноутбук", "price": 75000},
        {"id": 2, "name": "Мышь", "price": 1500},
        {"id": 3, "name": "Клавиатура", "price": 3500}
    ]
    return jsonify(products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)