from flask import Flask, jsonify, request
from flask_cors import CORS  # добавьте этот импорт
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'ваш-секретный-ключ-123'  # поменяйте на свой

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

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

@app.route('/api/users')
def users():
    return jsonify([{'id': user['id'], 'email': user['email']} for user in users_db])
#    return jsonify([1, 2])
        
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
    app.run(debug=True)