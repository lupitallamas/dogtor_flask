from dogtor.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String
#from datetime import datetime

class User(db.Model):
    id = mapped_column(Integer, primary_key=True)
    username= mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True)
    
class Owner(db.Model):
    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(length=50))
    last_name = mapped_column(String(length=50))
    phone = mapped_column(String(length=15))
    mobil = mapped_column(String(length=15))
    email = mapped_column(String) 

class Species(db.Model):
    """Pet Species"""
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    
class Pet(db.Model):
    """Pet Owner"""
    id_pet = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    age = mapped_column(Integer)
    owner = db.relationship(Owner, backref="pets")
    species = db.relationship(Species, backref= "pets")
    #create_at = mapped_column(datetime, d)
     
class Record(db.Model):
    """Medical record pets""" 
    id = mapped_column(Integer, primary_key=True)
    category = mapped_column(String)
    procedure = mapped_column(String)
    #date = mapped_column(datetime)
    pet = db.relationship(Pet, backref="pets")
    