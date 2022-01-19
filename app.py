import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']=True
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name','email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def get():
    return 'ok'