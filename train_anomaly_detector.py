# USAGE
# python train_anomaly_detector.py --dataset forest --model anomaly_detector.model

# import the necessary packages
from pyimagesearch.features import load_dataset
from sklearn.ensemble import IsolationForest
import argparse
import pickle

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to dataset of images")
ap.add_argument("-m", "--model", required=True,
	help="path to output anomaly detection model")
args = vars(ap.parse_args())

# load and quantify our image dataset
print("[INFO] preparing dataset...")
data, failed = load_dataset(args["dataset"], bins=(3, 3, 3))

# save list of paths with failed attemps
with open(r'failed_paths.txt', 'w') as fp:
    fp.write('\n'.join(failed))

# train the anomaly detection model
print("[INFO] fitting anomaly detection model...")
model = IsolationForest(n_estimators=1000, contamination='auto', 
    					n_jobs=5, max_features=3, random_state=42)
model.fit(data)

# serialize the anomaly detection model to disk
f = open(args["model"], "wb")
f.write(pickle.dumps(model))
f.close()