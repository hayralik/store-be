from flask import jsonify

def setup_get_products(app, Product):
    @app.route('/api/products')
    def get_products():
        products = Product.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description
        } for p in products])
