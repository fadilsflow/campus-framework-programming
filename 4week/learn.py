from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)

# Konfigurasi Database
app.config['SQLALCHEMY_DATABASE_URL']
