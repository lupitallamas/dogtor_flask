
from flask import request
from dogtor.db  import db
from . import api
from .models import Owner,Species,Pet,Record,Category
from datetime import datetime, date
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
def owners_endpoint(owner_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if owner_id is not None:
        owner = Owner.query.get_or_404(owner_id, "Owner not found")
        if request.method == "GET":
            return {"id": owner.id, "first_name": owner.first_name, "last_name":owner.last_name}

        if request.method == "PUT":
            owner.first_name = data["first_name"]
            owner.last_name = data["last_name"]
            owner.phone = data["phone"]
            owner.mobile = data["mobile"]
            owner.email = data["email"] 
            
            msg = f"Owner: {owner.id}  {owner.first_name} {owner.last_name} modified"

        if request.method == "DELETE":
            pet = Pet.query.filter(Pet.owner_id != owner_id)
            if  pet  is None:
                db.session.delete(owner)
                msg = f"Owner: {owner.id}  {owner.first_name} {owner.last_name} deleted"
            else:
                msg = f"Owner: {owner.id}  {owner.first_name} {owner.last_name} not deleted"
        db.session.commit()
        return {"detail": msg}

    if request.method == "GET":
        owners = Owner.query.all()
        return [{"id": owner.id, "first_name": owner.first_name, "last_name":owner.last_name, "email": owner.email} for owner in owners]

    if request.method == "POST":
        owner = Owner(
            first_name = data["first_name"],
            last_name = data["last_name"],
            phone = data["phone"],
            mobile = data["mobile"],
            email = data["email"] 
        )
        db.session.add(owner)
        db.session.commit()

        return {"detail": f"Owner {owner.first_name} {owner.last_name} created successfully"}
       
    # if owner_id is not None:
    #     found_owner = None
    #     for owner in owners_data:
    #         if owner["id"] == owner_id:
    #             found_owner = owner       
    #     if request.method == "PUT":
    #         return {"detail": f"owner {found_owner['first_name']}' '{found_owner['last_name']} modified"}
    #     if request.method == "DELETE":
    #         return {"detail": f"owner {found_owner['first_name']}' '{found_owner['last_name']}  deleted"}
    #     return found_owner
    # if request.method == "POST":
    #     data = request.data
    #     return {"detail": f"owner {data['first_name']}' ' {data['last_name']} created"}
    # return owners_data

#--------------------------------------------------
"""Pet"""
@api.route("/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/pets/", methods=["GET", "POST"])
def pets_endpoinst(pet_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if pet_id is not None:
        pet = Pet.query.get_or_404(pet_id, "Pet not found") 
        if request.method == "GET":
            owner = Owner.query.get(pet.owner_id)
            specie = Species.query.get(pet.species_id)
            return {"id": pet.id, 
                    "name": pet.name, 
                    "species":specie.name,
                    "owner_id":owner.id,
                    "first_name:":owner.first_name, 
                    "last_name":owner.last_name
                    }
 
        if request.method == "PUT":
            owner = Owner.query.get_or_404(data["owner_id"], "Owner not found")
            specie =Species.query.get_or_404(data["species_id"], "Species not found")
            pet.name = data["name"]
            pet.age = data["age"]
            pet.owner_id= data["owner_id"]
            pet.species_id= data["species_id"]
            msg = f"Pet: {pet.id}  {pet.name} {pet.owner_id} modified"

        if request.method == "DELETE":
            record = Record.query.filter(Record.pet_id != pet_id)
            if  record  is None:
                db.session.delete(pet)
                msg = f"Pet: {pet.id}  {pet.name} {pet.owner_id} not deleted"
            else:
                msg = f"Pet: {pet.id}  {pet.name} {pet.owner_id} deleted"
            
        db.session.commit()
        return {"detail": msg}

    if request.method == "GET":
        pets = Pet.query.all()
        return [{"id": pet.id, "name": pet.name, "owner_id":pet.owner_id,
                 "species": pet.species_id} for pet in pets
                ]

    if request.method == "POST":
        owner = Owner.query.get_or_404(data["owner_id"], "Owner not found")
        specie =Species.query.get_or_404(data["species_id"], "Species not found")
        pet = Pet(
            name = data["name"],
            owner_id = data["owner_id"],
            age = data["age"],
            species_id = data["species_id"]
        )
        db.session.add(pet)
        db.session.commit()

        return {"detail": f"Pet {pet.name} {pet.owner_id}  {pet.species_id} created successfully"}
    # if pet_id is not None:
    #     found_pet = None
    #     for pet in pets_data:
    #         if pet["id"] == pet_id:
    #             found_pet = pet
    #     if request.method == "PUT":
    #         return {"detail": f"pet {found_pet} modified"}
    #     if request.method == "DELETE":
    #         return {"detail": f"pet {found_pet} deleted"}
    #     return found_pet
    # if request.method == "POST":
    #     data = request.data
    #     return {"detail": f"pet {data['name']} creat1ed"}
    # return pets_data
#----------------------------------------
"""Record"""
@api.route("/records/<int:record_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/records/", methods=["GET", "POST"])
def records_endpoints(record_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if record_id is not None:
        record = Record.query.get_or_404(record_id, "record not found") 
        if request.method == "GET":
            pet = Pet.query.get(record.pet_id)
            return {"id": record.id, 
                    "category": record.category, 
                    "procedure": record.procedure,
                    "pet_id":record.pet_id,
                    "category_id":record.category_id,
                    "date":record.date
                    }
 
        if request.method == "PUT":
            date=datetime.datetime.strptime(data["date"],'%d/%m/%Y')
            date=datetime.datetime.date(date)
            pet = Pet.query.get_or_404(data["pet_id"], "Pet not found")
            record.category = data["category"]
            record.procedure = data["procedure"]
            record.pet_id= data["pet_id"]
            record.date = date
            msg = f"Record: {record.id}  {record.category} {record.pet_id} modified"

        if request.method == "DELETE":
                db.session.delete(record)
                msg = f"Pet: {record.id}  {record.category} {record.pet_id} deleted"
            
        db.session.commit()
        return {"detail": msg}

    if request.method == "GET":
        records= Record.query.all()
        return  [{"record_id": record.id, "catecory": record.category, "pet_id":record.pet_id
                 } for record in records
                ]

    if request.method == "POST":
        pet = Pet.query.get_or_404(data["pet_id"], "Pet not found")
        date=datetime.datetime.strptime(data["date"],'%d/%m/%Y')
        date=datetime.datetime.date(date)
        record = Record (
            category = data["category"],
            procedure = data["procedure"],
            pet_id = data["pet_id"],
            category_id = data["category_id"],
            date = date
        )
        db.session.add(record)
        db.session.commit()

        return {"detail": f"Record {record.id} {record.category} {record.pet_id} created successfully"}
    
    # if record_id is not None:
    #     found_record = None
    #     for record in records_data:
    #         if record["id"] == record_id:
    #             found_record = record
    #     if request.method == "PUT":
    #         return {"detail": f"Record {found_record} modified"}
    #     if request.method == "DELETE":
    #         return {"detail": f"record {found_record} deleted"}
    #     return found_record
    # if request.method == "POST":
    #         data = request.data
    #         return {"detail": f"record {data['category']} created"}
    #return record_data
import datetime

@api.route("/categories/<int:categories_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/categories/", methods=["GET", "POST"])
def categories_endpoint(categories_id=None):
    try:
        data = request.get_json()
    except:
        pass
    if categories_id is not None:
        category = Category.query.get_or_404(categories_id, "Category not found")
        if request.method == "GET":
            return {"id": category.id, "name": category.name}

        if request.method == "PUT":
            category.name = data["name"]
            msg = f"category {category.name} modified"

        if request.method == "DELETE":
            db.session.delete(category)
            msg = f"category {category.name} deleted"
            

        db.session.commit()
        return {"detail": msg}

    if request.method == "GET":
        category = Category.query.all()
        return [{"id": categories.id, "name": categories.name} for categories in category]

    if request.method == "POST":
    
        category = Category(name=data["name"])
    

        db.session.add(category)
        db.session.commit()

        return {"detail": f"category {category.name} created successfully"}
    



@api.route("/species/<int:species_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/species/", methods=["GET", "POST"])
def species_endpoint(species_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if species_id is not None:
        species = Species.query.get_or_404(species_id, "Species not found")
        if request.method == "GET":
            return {"id": species.id, "name": species.name}

        if request.method == "PUT":
            species.name = data["name"]
            msg = f"species {species.name} modified"

        if request.method == "DELETE":
            db.session.delete(species)
            msg = f"species {species.name} deleted"

        db.session.commit()
        return {"detail": msg}

    if request.method == "GET":
        species = Species.query.all()
        return [{"id": species.id, "name": species.name} for species in species]

    if request.method == "POST":
    
        species = Species(name=data["name"])

        db.session.add(species)
        db.session.commit()

        return {"detail": f"species {species.name} created successfully"}
       