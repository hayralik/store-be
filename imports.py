from datetime import timedelta

from config_app import config_app
from create_db import create_db

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity