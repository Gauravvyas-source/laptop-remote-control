from flask import Blueprint
from utils.auth import is_authorized
from utils.responce import success,error
import os

lock_bp = Blueprint("lock", __name__)

@lock_bp.route("/lock")
def lock():
    try:
        if not is_authorized():
            return error("Unauthorized")
    
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return success({"status": "System Locked" })
    except Exception as e :
        return error(str(e))
    
    