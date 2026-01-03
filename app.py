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
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locked"


@app.route("/status")
def status():
    return success(get_status())
    


@app.route("/system-info")
def system_info():
  data = get_system_info()
  return success(data)
  


@app.route("/battery")
def battery():
   percent = get_battery_percentage()
   return success({
       "battery" : percent
   })

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
