from flask import Flask, jsonify
from flask_cors import CORS
import os
from lib import db

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Enable CORS for frontend
    CORS(app)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:root@localhost:8889/flask-week-4'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Initialize lib
    db.init_app(app)
    
    # Import and register blueprints or routes
    from views.routes import init_routes
    init_routes(app)
    
    # Import API routes
    from controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
    
    # API Routes
    app.add_url_rule('/api/users', 'api_create_user', create_user, methods=['POST'])
    app.add_url_rule('/api/users', 'api_get_users', get_users, methods=['GET'])
    app.add_url_rule('/api/users/<int:user_id>', 'api_get_user', get_user, methods=['GET'])
    app.add_url_rule('/api/users/<int:user_id>', 'api_update_user', update_user, methods=['PUT'])
    app.add_url_rule('/api/users/<int:user_id>', 'api_delete_user', delete_user, methods=['DELETE'])
    
    # API Info endpoint
    @app.route('/api')
    def api_info():
        return jsonify({
            'name': 'User Management API',
            'version': '1.0',
            'endpoints': {
                'list_users': {'method': 'GET', 'url': '/api/users'},
                'create_user': {'method': 'POST', 'url': '/api/users'},
                'get_user': {'method': 'GET', 'url': '/api/users/<id>'},
                'update_user': {'method': 'PUT', 'url': '/api/users/<id>'},
                'delete_user': {'method': 'DELETE', 'url': '/api/users/<id>'}
            }
        })
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    
    # Run the app
    app.run(debug=True, port=5000)
