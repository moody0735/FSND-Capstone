import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
database_path = "postgres://{}:{}@{}/{}".format('postgres', '9520099', 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    return db





# ---------------------------------------------------------
# Models.
# ---------------------------------------------------------

class Actor(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(80), unique=True)
    age = Column(Integer)
    gender = Column(String(80), nullable=True)

  
    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

  
    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())



class Movie(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(80), unique=True)
    release =  Column(Integer, nullable=False)

  
    def short_movie(self):
        return {
            'id': self.id,
            'title': self.title
        }

  
    def long_movie(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short_movie())