from flask import request
from flask_jwt_extended import jwt_required

def setup_add_product(app, Product, db):
    @app.route('/api/products', methods=['POST'])
    @jwt_required()
    def add_product():
        data = request.get_json()
        product = Product(
            name=data['name'],
            price=data['price'],
            description=data.get('description', 'ABC')
        )
        db.session.add(product)
        db.session.commit()
        return {'message': 'Product added', 'id': product.id}, 201
