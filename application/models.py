from application import db
import random

#class Image(db.model):
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(32), unique=True, nullable=False)
    #head_figure = db.Column(db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__():
        return '<ID: %s, Username: %s>' %(self.id, self.username)
    
