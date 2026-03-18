from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

from config_app import config_app
from create_db import create_db

from routes.home import setup_home
from routes.users import setup_users
from routes.register import setup_register
from routes.login import setup_login
from routes.profile import setup_profile
from routes.get_products import setup_get_products
from routes.add_product import setup_add_product
