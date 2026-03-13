from app import app, db, Product

products_data = [
    {"name": "Ноутбук", "price": 75000, "description": "Мощный ноутбук для работы и игр"},
    {"name": "Мышь", "price": 1500, "description": "Беспроводная мышь"},
    {"name": "Клавиатура", "price": 3500, "description": "Механическая клавиатура"},
    {"name": "Монитор", "price": 18000, "description": "4K монитор 27 дюймов"},
    {"name": "Жесткий диск", "price": 2000, "description": "Надежный жесткий диск объемом 4 ТБ"}
]

with app.app_context():
    for item in products_data:
        product = Product(
            name=item["name"],
            price=item["price"],
            description=item["description"]
        )
        db.session.add(product)
    db.session.commit()
    print("Товары добавлены")