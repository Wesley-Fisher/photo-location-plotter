SHELL := /bin/bash

ubuntu:
	docker build -t photo_location_plotter:latest -f Dockerfile.Ubuntu ..

project:
	test $(PROJECT)
	docker run \
	-v "${PWD}/../photo_location_plotter:/workspace/photo_location_plotter:rw" \
	-v "${PWD}/../projects:/workspace/projects:rw" \
	-v "${PWD}/../test:/workspace/test:rw" \
	-v "${PWD}/../run.py:/workspace/run.py:rw" \
	photo_location_plotter:latest \
	python3 /workspace/run.py $(PROJECT)