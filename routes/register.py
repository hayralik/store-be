from flask import request

def setup_register(app, User, bcrypt, db):
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
