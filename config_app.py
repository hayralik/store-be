from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


# ==========================================================
# БЛОК 2: Конфигурация приложения (Flask, CORS, bcrypt, jwt)
# Настраивается CORS, чтобы React-фронтенд мог общаться с бэкендом
# Инициализируются расширения: bcrypt для шифрования паролей и JWT для токенов

def config_app(app):
    CORS(app)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)
    return bcrypt, jwt  # возвращаем созданные объекты

