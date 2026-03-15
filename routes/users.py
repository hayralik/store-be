from flask import jsonify

def setup_users(app, User):
    @app.route('/api/users')
    def users():
        users_list = User.query.all()
        return jsonify([{'id': u.id, 'email': u.email} for u in users_list])
