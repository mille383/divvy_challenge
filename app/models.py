from datetime import datetime as dt
from app import db
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    password = db.Column(db.String)

    def save(self):
        # set password as the hashed password from set_password method
        self.set_password(self.password)
        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        for attr in ['first_name', 'last_name', 'email', 'password']:
            if attr in data:
                if attr == 'email':
                    setattr(self, attr, data[attr].lower())
                else:
                    setattr(self, attr, data[attr])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_on': dt.strftime(self.created_on, '%m/%d/%Y'),
            'password': self.password
        }

    def __repr__(self):
        return f'<User: {self.email}>'

    def set_password(self, pword):
        self.password = generate_password_hash(pword)

    def check_password(self, pword):
        return check_password_hash(self.password, pword)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    body = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=dt.utcnow)

    # def from_dict(self):
    #     pass

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            # 'image': self.image,
            # 'title': self.title,
            'body': self.body,
            'created_on': dt.strftime(self.created_on, '%m/%d/%Y')
        }

    def __repr__(self):
        return f'<Post: [{self.email}]: {self.body[:20]}...>'