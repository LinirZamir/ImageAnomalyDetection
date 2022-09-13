
import os

directory = "mushrooms"

anom_list = [file for file in os.listdir("anomalies")]

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename in anom_list:
            os.unlink(os.path.join(root,filename))
            