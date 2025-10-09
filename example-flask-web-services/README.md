# Flask API Project

A simple Flask-based REST API web service with CRUD operations for user management.

## Features

- RESTful API endpoints
- CORS support
- JSON responses
- Error handling
- Health check endpoint
- User CRUD operations

## API Endpoints

### Base URL

```
http://localhost:5000
```

### Available Endpoints

| Method | Endpoint          | Description                    |
| ------ | ----------------- | ------------------------------ |
| GET    | `/`               | Home page with API information |
| GET    | `/api/health`     | Health check endpoint          |
| GET    | `/api/users`      | Get all users                  |
| GET    | `/api/users/{id}` | Get user by ID                 |
| POST   | `/api/users`      | Create new user                |
| PUT    | `/api/users/{id}` | Update user by ID              |
| DELETE | `/api/users/{id}` | Delete user by ID              |

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the configuration file and modify as needed:

```bash
cp config.env .env
```

Edit `.env` file with your settings:

```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
PORT=5000
```

### 3. Run the Application

#### Development Mode

```bash
python app.py
```

#### Production Mode (using Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

The API will be available at `http://localhost:5000`

## API Usage Examples

### Get All Users

```bash
curl http://localhost:5000/api/users
```

### Create a New User

```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "email": "alice@example.com"}'
```

### Get User by ID

```bash
curl http://localhost:5000/api/users/1
```

### Update User

```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

### Delete User

```bash
curl -X DELETE http://localhost:5000/api/users/1
```

### Health Check

```bash
curl http://localhost:5000/api/health
```

## Project Structure

```
campus-framework-programming/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── config.env         # Environment configuration template
└── README.md          # This file
```

## Development

- The application runs in debug mode when `FLASK_ENV=development`
- CORS is enabled for all routes
- Error handling is implemented for common HTTP errors
- All responses are in JSON format

## Production Deployment

For production deployment:

1. Set `FLASK_ENV=production` in your environment
2. Use a strong `SECRET_KEY`
3. Use a production WSGI server like Gunicorn
4. Consider using a reverse proxy like Nginx
5. Set up proper logging and monitoring
