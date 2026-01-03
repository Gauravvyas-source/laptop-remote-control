import platform


def get_system_info():
    return {
        "os" : platform.system()
    }


def get_status():
    return{
        "connected":True
    }