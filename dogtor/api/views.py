
from flask import request
from . import api
from .models import Owner,Species,Pet,Record

from dogtor.db import db


users_data = [
        {"id": 1, "username": "user0", "email": "user0@kodemia.mx"},
        {"id": 2, "username": "user1", "email": "user1@kodemia.mx"},
        {"id": 3, "username": "user2", "email": "user2@kodemia.mx"},
    ]
owners_data = [
        {"id": 1, "first_name": "Miren", "last_name": "Llamas","email":"miren@kodemi.com"},
        {"id": 2, "first_name": "Jorge", "last_name": "Ramirez","email":"jorge@kodemi.com"},
        {"id": 3, "first_name": "Alfredo", "last_name": "Altamirano","email":"alfredo@kodemi.com"},
    ]
pets_data=[
        {"id": 1, "name": "nala", "age": "5", "owner": "1","specie": "perro"},
        {"id": 2, "name": "Clhoe", "age": "2", "owner": "1","specie": "gato"},
        {"id": 3, "name": "dixie", "age": "10", "owner": "2","specie": "conejo"},        
    ]
"""Record"""
record_data =[
        {"id": 1, "category": 0 , "procedure": "desparacitacion", "date": "30/10/24","pet": "1"},
        {"id": 2, "category": 3 , "procedure": "consulta", "date": "30/10/24","pet": "2"},
        {"id": 3, "category": 4 , "procedure": "desparacitacion", "date": "30/10/24","pet": "3"},
         
]

# @api.router("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
# @users_blueprint.router
# def get_change_delete_user(user_id):
#     """Single user interaction route"""
#     found_user = None
#     for user in users_data:
#         if user["id"] == user_id:
#             found_user = user
#     if request.method == "PUT":
#         return {"detail": f"user {found_user['username']} modified"}
#     if request.method == "DELETE":
#         return {"detail": f"user {found_user['username']} deleted"}
#     return found_user

# @app.route("/users/", methods=["GET", "POST"])
# def get_or_create_users():
#     """All users interaction route"""
#     if request.method == "POST":
#         data = request.get_json()
#         return {"detail": f"user {data['username']} created"}
#     return users


    
# @app.post("/users/auth")
# def auth():
#     data = request.data
#     return data
    
@api.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/users/", methods=["GET", "POST"])
def users(user_id=None):
    if user_id is not None:
        found_user = None
        for user in users_data:
            if user["id"] == user_id:
                found_user = user

        if request.method == "PUT":
            return {"detail": f"user {found_user['username']} modified"}
        if request.method == "DELETE":
            return {"detail": f"user {found_user['username']} deleted"}

        return found_user

    if request.method == "POST":
        data = request.data
        return {"detail": f"user {data['username']} created"}
    return users_data
       
 
@api.route("/owners/<int:owner_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/owners/", methods=["GET", "POST"])
def owners(owner_id=None):
    if owner_id is not None:
        found_owner = None
        for owner in owners_data:
            if owner["id"] == owner_id:
                found_owner = owner       
        if request.method == "PUT":
            return {"detail": f"owner {found_owner['first_name']}' '{found_owner['last_name']} modified"}
        if request.method == "DELETE":
            return {"detail": f"owner {found_owner['first_name']}' '{found_owner['last_name']}  deleted"}
        return found_owner
    if request.method == "POST":
        data = request.data
        return {"detail": f"owner {data['first_name']}' ' {data['last_name']} created"}
    return owners_data

#--------------------------------------------------
"""Pet"""
@api.route("/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/pets/", methods=["GET", "POST"])
def pets(pet_id=None):
    if pet_id is not None:
        found_pet = None
        for pet in pets_data:
            if pet["id"] == pet_id:
                found_pet = pet
        if request.method == "PUT":
            return {"detail": f"pet {found_pet} modified"}
        if request.method == "DELETE":
            return {"detail": f"pet {found_pet} deleted"}
        return found_pet
    if request.method == "POST":
        data = request.data
        return {"detail": f"pet {data['name']} creat1ed"}
    return pets_data
#----------------------------------------
"""Record"""
@api.route("/records/<int:record_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/records/", methods=["GET", "POST"])
def records(record_id=None):
    if record_id is not None:
        found_record = None
        for record in records_data:
            if record["id"] == record_id:
                found_record = record
        if request.method == "PUT":
            return {"detail": f"Record {found_record} modified"}
        if request.method == "DELETE":
            return {"detail": f"record {found_record} deleted"}
        return found_record
    if request.method == "POST":
            data = request.data
            return {"detail": f"record {data['category']} created"}
    return record_data
# @api.route("/species/<int:species_id>", method=["GET","PUT","DELETE"])
# @api.route("/species/", methods=["GET","POST"])
# def species_endpoint(species_id = None):
#     if request.method == "GET":
#         species_all = Species.query.all()
#         return[{"id":}]
#     data = request.get_json()
#     species_instance = models.Species(name=data["name"])
#     db.session.add(species_instance)
#     db.session.commit()
#     return data
    
       