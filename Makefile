ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

init-dev:
	pip install compile-env==0.4.1

compile-env:
	cd ${ROOT_DIR}/env/dev && compile-env env-spec.yaml

create-opt-paths:
	sudo mkdir -p /opt/projects/holiplan/backend
	sudo echo     "- cmd: echo 'start of the fish history'" >> /opt/projects/holiplan/backend/fish_history
	sudo mkdir -p /opt/projects/holiplan/backend/ipython
	sudo mkdir -p /opt/projects/holiplan/backend/assets
	sudo touch    /opt/projects/holiplan/backend/pytest_report.html
	sudo mkdir -p /opt/projects/holiplan/backend/media
	sudo mkdir -p /opt/projects/holiplan/backend/static
	sudo chmod -R 777 /opt/projects/holiplan
