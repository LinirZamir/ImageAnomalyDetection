# USAGE
# python test_anomaly_detector.py --model anomaly_detector.model --image examples/highway_a836030.jpg

# import the necessary packages
from genericpath import exists
from pyimagesearch.features import quantify_image
import pickle
import cv2
import os
import shutil

# load the anomaly detection model
print("[INFO] loading anomaly detection model...")
model = pickle.loads(open("anomaly_detector.model", "rb").read())


# assign directory
directory = 'mushrooms'

anomalies = []
print("[INFO] making predictions...")

for root, dirs, files in os.walk(directory):
    for filename in files:
        if '.jpg' in filename:
            #print(os.path.join(root, filename))
            image = cv2.imread(os.path.join(root, filename))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            features = quantify_image(hsv, bins=(3, 3, 3))

            preds = model.predict([features])[0]
            if preds == -1:
                anomalies.append(os.path.join(root, filename))


anom_directory = 'anomalies'

if os.path.exists(anom_directory):
    os.rmdir(anom_directory)
os.mkdir(anom_directory)

for img in anomalies:
    shutil.copy2(img, 'anomalies')

print(f"[INFO] Found {len(anomalies)} anomalies")

