from flask import Blueprint

api = Blueprint("api",__name__, url_prefix="/api")
from . import views
from . import models
#asi empienzas las url de esta como api como app -->/api/
#/api/login
#/api/logout
#/api/signup