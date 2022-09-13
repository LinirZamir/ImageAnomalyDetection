
create_env: 
	conda env create -f environment.yml

activate_env:
	conda activate image_anom_detection

update_env:
	conda env update --prefix ./env --file environment.yml  --prune

clean_folder_names:
	python clean_folder_names.py

remove_failed:
	python remove_failed_images.py

train:
	python train_anomaly_detector.py --dataset mushrooms --model anomaly_detector.model

test_normal:
	python test_anomaly_detector.py --model anomaly_detector.model \
	--image mushrooms/Lactarius-torminosus/2e66ce78-d505-4b9a-82f9-23f2a8feac3f.jpg

test_anom:
	python test_anomaly_detector.py --model anomaly_detector.model \
	--image examples/highway_a836030.jpg

test_anom2:
	python test_anomaly_detector.py --model anomaly_detector.model \
	--image examples/Rplot.jpg

test_anom3:
	python test_anomaly_detector.py --model anomaly_detector.model \
	--image examples/coast_osun52.jpg

test_anom4:
	python test_anomaly_detector.py --model anomaly_detector.model \
	--image mushrooms/Langermannia-gigantea/99f9025d-1a7b-4f4f-9776-4fd6bbf0d951.jpg

run_on_all:
	python run_on_all.py

remove_outliers:
	python remove_outliers.py

check_images_per_class:
	python check_images_per_class.py
	