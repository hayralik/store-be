from flask_jwt_extended import jwt_required, get_jwt_identity

def setup_profile(app, User):
    @app.route('/api/profile', methods=['GET'])
    @jwt_required()
    def profile():
        current_user_id = int(get_jwt_identity())
        
        # Ищем пользователя по id
        user = User.query.filter_by(id=current_user_id).first()
        if user:
            return {'id': user.id, 'email': user.email}, 200
        
        return {'message': 'User not found'}, 404
