import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']=True
db = SQLAlchemy(app)

#Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)

@app.route('/')
def get():
    return 'ok'