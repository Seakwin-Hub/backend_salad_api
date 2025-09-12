from urllib.parse import quote
from flask import Flask, request, json, jsonify, render_template
from flask_restful import Api
import logging, os
from flask_sqlalchemy import SQLAlchemy

url = quote('localhost')
port = quote('3306')
username = quote('root')
password =  quote('Seakwin$$$6050')
mysqldb = quote('dbsaladdiseases')
# config file
app = Flask(__name__)

api = Api(app)
if os.environ.get('DATABASE_URL'):
    # For production (Render)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # Fix for PostgreSQL URL format in SQLAlchemy
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)
else:
    # For local development
    url = quote('localhost')
    port = quote('3306')
    username = quote('root')
    password = quote('Seakwin$$$6050')
    mysqldb = quote('dbsaladdiseases')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + url + ':' + port + '/' + mysqldb


# log = logging.getLogger('werkzeug')
# log.disabled = True
    
app.config["SESSION_PERMANENT"] = False
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + url + ':' + port + '/' + mysqldb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['CORS_HEADERS'] = 'Content-Type'

DEBUG = False

db = SQLAlchemy(app)

