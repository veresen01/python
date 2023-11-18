from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    # lastname = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password,password)


    def __repr__(self):
        return f'User({self.name})'
