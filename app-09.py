# VS Code: все предупреждения ниже можно игнорировать
# CORS, db инициализируются внутри config_app и create_db

from dotenv import load_dotenv
load_dotenv()

import os
from imports import *

# Определяем окружение
is_production = os.environ.get('RENDER') or os.environ.get('PRODUCTION')

if is_production:
    # В продакшене используем PostgreSQL URL из переменных окружения Render
    database_url = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
else:
    # Локально - SQLite
    database_url = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'shop.db')

app = Flask(__name__, 
            static_folder='../client/dist',  # для React build
            template_folder='../client/dist')

# Конфигурация
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'ваш-секретный-ключ-для-разработки')

# Инициализация
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db.init_app(app)

# Создание таблиц (вместо миграций для простоты)
with app.app_context():
    db.create_all()

# Ваши роуты (или импорты из routes)
# ... остальной код

# Для клиентской маршрутизации React (важно!)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path and (path.startswith('api/') or path == 'api'):
        return {'error': 'Not found'}, 404
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)