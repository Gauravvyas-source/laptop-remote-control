from flask import request

SECRET_TOKEN = "123456"
 
def is_authorized():
 
  token=request.args.get("token")
  return token == SECRET_TOKEN
