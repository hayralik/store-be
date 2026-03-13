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


class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Проверка на существующего пользователя через базу
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {'message': 'User already exists'}, 400

    if len(password) < 6:
        return {'message': 'The password must contain at least 6 characters!'}, 400

    # Хешируем пароль
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Создаём нового пользователя через модель
    new_user = User(email=email, password=hashed_password)
    
    # Сохраняем в базу
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User created successfully'}, 201


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


@app.route('/api/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = int(get_jwt_identity())
    
    # Ищем пользователя по id
    user = User.query.filter_by(id=current_user_id).first()
    if user:
        return {'id': user.id, 'email': user.email}, 200
    
    return {'message': 'User not found'}, 404


@app.route('/api/users')
def users():
    users_list = User.query.all()
    return jsonify([{'id': u.id, 'email': u.email} for u in users_list])


@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/api/products')
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description
    } for p in products])


@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        description=data.get('description', '')
    )
    db.session.add(product)
    db.session.commit()
    return {'message': 'Product added', 'id': product.id}, 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)