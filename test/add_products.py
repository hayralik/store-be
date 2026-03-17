import requests
from base_url import base_url


products_data = [
    {"name": "Ноутбук", "price": 75000, "description": "Мощный ноутбук для работы и игр"},
    {"name": "Мышь", "price": 1500, "description": "Беспроводная мышь"},
    {"name": "Клавиатура", "price": 3500, "description": "Механическая клавиатура"},
    {"name": "Монитор", "price": 18000, "description": "4K монитор 27 дюймов"},
    {"name": "Жесткий диск", "price": 2000, "description": "Надежный жесткий диск объемом 4 ТБ"}
]

def post(url, product):
    print(requests.post(url, json=product).json())

for product in products_data:
    post(base_url + '/api/products', product)
    