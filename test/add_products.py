import requests

products_data = [
    {"name": "Ноутбук", "price": 75000, "description": "Мощный ноутбук для работы и игр"},
    {"name": "Мышь", "price": 1500, "description": "Беспроводная мышь"},
    {"name": "Клавиатура", "price": 3500, "description": "Механическая клавиатура"},
    {"name": "Монитор", "price": 18000, "description": "4K монитор 27 дюймов"},
    {"name": "Жесткий диск", "price": 2000, "description": "Надежный жесткий диск объемом 4 ТБ"}
]
url = "http://localhost:5000"

def post(url, product):
    print(requests.post(url, json=product).json())

for product in products_data:
    post(url + '/api/products', product)
    