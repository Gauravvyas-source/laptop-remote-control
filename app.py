from flask import Flask, request, jsonify
from routes.status import status_bp
from routes.battery import battery_bp
from routes.lock import lock_bp
from utils.responce import success
from services.battery_service import get_battery_percentage
from services.system_service import get_system_info
from services.system_service import get_status

import psutil
import platform


app = Flask(__name__)
app.register_blueprint(status_bp)
app.register_blueprint(battery_bp)
app.register_blueprint(lock_bp)

@app.route("/")
def home():
    return "Server running"


   


@app.route("/system-info")
def system_info():
   try:
     data = get_system_info()
     return success(data)
   except Exception as e : 
       return error (str(e),500)
  

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
