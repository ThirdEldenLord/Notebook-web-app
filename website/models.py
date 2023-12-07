from website import data_base
from flask_login import UserMixin
from sqlalchemy.sql import func

#Class for notes in our data base
class Note(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    note = data_base.Column(data_base.String(20000))
    date = data_base.Column(data_base.DateTime(timezone=True), default=func.now())
    user_id = data_base.Column(data_base.Integer, data_base.ForeignKey('user.id'))

#Class for users
class User(data_base.Model, UserMixin):
    id = data_base.Column(data_base.Integer, primary_key=True)
    first_name = data_base.Column(data_base.String(200))
    email = data_base.Column(data_base.String(200), unique=True)
    password = data_base.Column(data_base.String(200))
    notes = data_base.relationship('Note')
    