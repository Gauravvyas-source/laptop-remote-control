from flask import Flask, request, jsonify
from utils.responce import success
from services.battery_service import get_battery_percentage
from services.system_service import get_system_info
from services.system_service import get_status
import os
import psutil
import platform


app = Flask(__name__)
SECRET_TOKEN = "123456"

@app.route("/")
def home():
    return "Server running"

@app.route("/lock")
def lock():
    try:
      os.system("rundll32.exe user32.dll,LockWorkStation")
      return "Locked"
    except Exception as e : 
       return error (str(e),500)


@app.route("/status")
def status():
    try:
        return success(get_status())
    except Exception as e:
        return error(str(e),500)


@app.route("/system-info")
def system_info():
   try:
     data = get_system_info()
     return success(data)
   except Exception as e : 
       return error (str(e),500)
  


@app.route("/battery")
def battery():
   try:
       
       percent = get_battery_percentage()
       return success({
                "battery" : percent
             })
   except Exception as e:
      return error (str(e),500)



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
