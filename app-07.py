from imports import *

#1. создается основной объект Flask, который будет управлять всем приложением
app = Flask(__name__)

#2. Конфигурация приложения (CORS, bcrypt, jwt)
bcrypt, jwt = config_app(app)

#3. База данных (путь к БД, создание db, модели)
db, User, Product = create_db(app)

#print("CORS настроен?", app.after_request_funcs)  # должна быть не пустая


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

"""
@app.route('/api/products/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description
    })
"""

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