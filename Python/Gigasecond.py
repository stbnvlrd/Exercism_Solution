from datetime import datetime, timedelta
def add(time): 
    time_after = time + timedelta(0, 1000000000)
    return time_after