from src import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String (120), index = True, unique=True)
    password_hash = db.Column(db.String(1200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def check_user(self):
        return User.query.filter_by(email=self.email).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

db.create_all()