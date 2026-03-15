from flask_sqlalchemy import SQLAlchemy
import os

# БЛОК 3: База данных (путь к БД, создание db, модели)
# Задается путь к файлу базы данных SQLite
# Отключается ненужное отслеживание изменений SQLAlchemy
# Создается объект db для работы с базой данных через SQLAlchemy
# Определяется модель User (таблица users) с полями id, email, password
# Определяется модель Product (таблица products) с полями id, name, price, description
def create_db(app):
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
        
    return db, User, Product
