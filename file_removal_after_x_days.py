import datetime
import os
import time

path = r"C:/Users/liviu/OneDrive/Desktop/Python Projects/Coding stuff/results/"
now = time.time()
days_until_removal = 7

for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)): #file check
        creation_time = os.path.getctime(os.path.join(path, filename))
        UTC_time = datetime.datetime.fromtimestamp(creation_time, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        if os.path.getctime(os.path.join(path, filename)) < now - days_until_removal * 86400: #file removal after x days
            print(filename)
            # os.remove(os.path.join(path, filename))
