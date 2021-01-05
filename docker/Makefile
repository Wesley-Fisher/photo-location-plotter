SHELL := /bin/bash

ubuntu:
	docker build -t photo_location_plotter:latest -f Dockerfile.Ubuntu ..

test:
	docker run photo_location_plotter:latest \
	python3 run.py test_project