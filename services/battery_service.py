import psutil
def get_battery_percentage():
    bat = psutil.sensors_battery()
    if bat is None:
        return None
    
    return bat.percent