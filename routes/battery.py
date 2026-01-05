from flask import Blueprint
from utils.auth import is_authorized
from utils.responce import success,error
from services.battery_service import get_battery_percentage

battery_bp = Blueprint("battery",__name__)

@battery_bp.route("/battery")
def battery():
 try: 
     if not is_authorized():
         return error("Unauthorized")
     percent = get_battery_percentage()
     return success({
         "battery":percent
     })
 except Exception as e :
     return error(str(e))