.PHONY: lock, quality, tests

build:
	@echo "Building docker image..."
	@docker build -f Dockerfile -t web_scrapping:1.0 .

start:
	@echo "Starting service"
	@docker run --network host --name web_scrapping web_scrapping:1.0

clear:
	@echo "Remove Docker containers"
	@docker rm -f web_scrapping

#Invoke the poetry lock process
lock:
	@echo "Starting poetry lock process..."
	@python3 -m pip install -q poetry==1.8.5
	@poetry lock

help:
	@echo "Help to use"

clear_csv:
	@rm *.csv

quality:
	@echo "Starting quality process..."
	@poetry install --with dev
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files

tests:
	@echo "Starting tests processes"
	@poetry install --with dev
	@poetry run pytest --cov=tests --cov-fail-under=70

install: #make sure, python 3.12, python-pip and python-venv are installed in current machine
	@rm -rf .venv/
	@python3 -m venv .venv/
	@source ./.venv/bin/activate
	@python -m pip install -q poetry==1.8.5
	@poetry install

run:
	@python web_scrapping.py 851
