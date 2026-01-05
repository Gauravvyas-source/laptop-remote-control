from flask import jsonify

def success(data=None):
    return jsonify({
        "success":True,
        "data": data,
        "error":None

    })
def error(message, code = 400):
    response = jsonify({
        "success": False,
        "data": None,
        "error": message
    })
    response.status_code = code
    return response

    