from imports import *
from dotenv import load_dotenv
load_dotenv()

#1. создается основной объект Flask, который будет управлять всем приложением
app = Flask(__name__)

#2. Конфигурация приложения (CORS, bcrypt, jwt)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
bcrypt, jwt = config_app(app)

#3. База данных (путь к БД, создание db, модели)
db, User, Product = create_db(app)

#print("CORS настроен?", app.after_request_funcs)  # должна быть не пустая

setup_home(app)
setup_users(app, User)

setup_register(app, User, bcrypt, db)
setup_login(app, User, bcrypt)
setup_profile(app, User)

setup_get_products(app, Product)
setup_add_product(app, Product, db)


@app.route('/api/products/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description
    })



from sqlalchemy import text

@app.route('/debug/types')
def debug_types():
    result = db.session.execute(text('SELECT id, typeof(id) FROM products'))
    types = [{'id': row[0], 'type': row[1]} for row in result]
    return jsonify(types)

"""
@app.route('/debug/types')
def debug_types():
    result = db.session.execute('SELECT id, typeof(id) FROM products')
    types = [{'id': row[0], 'type': row[1]} for row in result]
    return jsonify(types)
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)