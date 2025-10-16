# Flask SQLAlchemy Tutorial

Proyek ini adalah implementasi Flask dengan SQLAlchemy untuk belajar database operations.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Setup MySQL database:

```sql
CREATE DATABASE flask-week-4;
```

3. Set environment variable (opsional):

```bash
export DATABASE_URL="mysql+pymysql://root:root@localhost:8889/flask-week-4"
```

4. Jalankan aplikasi:

```bash
python main.py
```

## Features

- 🌐 **Web Frontend**: Interface web yang interaktif untuk testing CRUD
- 🔧 **REST API**: API endpoints untuk semua operasi database
- 📊 **Database Management**: MySQL dengan SQLAlchemy ORM
- ✅ **Error Handling**: Validasi dan error handling yang lengkap

## API Endpoints

- `GET /` - Frontend web interface
- `GET /api` - Info API
- `GET /users` - Dapatkan semua users
- `POST /users` - Buat user baru
- `GET /users/<id>` - Dapatkan user berdasarkan ID
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Hapus user

## Cara Menggunakan

### 1. Web Frontend (Recommended)

1. Jalankan aplikasi: `python main.py`
2. Buka browser: `http://localhost:5000`
3. Gunakan interface web untuk testing CRUD operations

### 2. API Testing dengan Script

```bash
python test_api.py
```

### 3. Manual API Testing

#### Membuat User Baru

```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

#### Mendapatkan Semua Users

```bash
curl http://localhost:5000/users
```

#### Update User

```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

#### Hapus User

```bash
curl -X DELETE http://localhost:5000/users/1
```
