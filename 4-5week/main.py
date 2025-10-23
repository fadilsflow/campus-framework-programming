from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

# Inisialisasi Flask app
app = Flask(__name__) 


# Enable CORS untuk frontend
CORS(app)

# Konfigurasi Database
# Menggunakan MySQL dengan konfigurasi yang fleksibel
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'mysql+pymysql://root:root@localhost:8889/flask-week-4'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi SQLAlchemy
db = SQLAlchemy(app)

# Model untuk User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

# Routes untuk CRUD operations

# CREATE - Membuat user baru
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        # Validasi input
        if not data or not data.get('name') or not data.get('email'):
            return jsonify({'error': 'Name dan email harus diisi'}), 400

        # Cek apakah email sudah ada
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'Email sudah terdaftar'}), 400

        # Buat user baru
        new_user = User(
            name=data['name'],
            email=data['email']
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': 'User berhasil dibuat',
            'user': new_user.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# READ - Mendapatkan semua users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify({
            'users': [user.to_dict() for user in users],
            'total': len(users)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# READ - Mendapatkan user berdasarkan ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return jsonify({'user': user.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# UPDATE - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        data = request.get_json()

        # Update field yang ada
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            # Cek apakah email sudah digunakan user lain
            existing_user = User.query.filter(
                User.email == data['email'],
                User.id != user_id
            ).first()
            if existing_user:
                return jsonify({'error': 'Email sudah digunakan user lain'}), 400
            user.email = data['email']

        db.session.commit()

        return jsonify({
            'message': 'User berhasil diupdate',
            'user': user.to_dict()
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# DELETE - Hapus user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User berhasil dihapus'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route untuk frontend
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk API info
@app.route('/api')
def api_info():
    return jsonify({
        'message': 'Flask SQLAlchemy API',
        'endpoints': {
            'GET /users': 'Mendapatkan semua users',
            'POST /users': 'Membuat user baru',
            'GET /users/<id>': 'Mendapatkan user berdasarkan ID',
            'PUT /users/<id>': 'Update user',
            'DELETE /users/<id>': 'Hapus user'
        }
    })

# Fungsi untuk membuat tabel database

def create_tables():
    db.create_all()
    print("Database tables created!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database initialized!")

    app.run(debug=True, host='0.0.0.0', port=5000)
