from flask import Blueprint
from utils.auth import is_authorized
from utils.responce import success, error
from services.system_service import get_system_info

status_bp = Blueprint("status",__name__)

@status_bp.route("/status")
def status():
  try:
      if not is_authorized():
          return error("Unauthorized")
      data = get_system_info()
      return success(data)
  except Exception as e :
     return error(str(e))

