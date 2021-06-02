from datetime import datetime as dt
from app import db
# from flask_login import UserMixin
# from app import login_manager
# from werkzeug.security import check_password_hash, generate_password_hash


class Ride(db.Model):
    __tablename__ = 'divvy'

    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime)
    stoptime = db.Column(db.DateTime)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String(45))
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String(45))
    usertype = db.Column(db.String(45))
    gender = db.Column(db.String(15))
    birthday = db.Column(db.String(20)) # getting some errors with this as it's all blank
    trip_duration = db.Column(db.Integer)

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'email': self.email,
    #         'body': self.body,
    #         'user': User.query.get(self.user_id).to_dict(),
    #         'created_on': dt.strftime(self.created_on, '%m/%d/%Y')
    #     }

    # def __repr__(self):
    #     return f'<Post: [{self.email}]: {self.body[:20]}...>'