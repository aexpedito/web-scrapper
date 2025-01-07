help:
	@echo "Help to use"

clear_csv: #deleta o arquivo .csv gerado
	@rm *.csv

enable_venv:  #make sure python 3.12, python-pip and python3-venv are installed in current machine
	@rm -rf .venv/
	@python3 -m venv .venv/

install: #enable virtualenv before make install: source .venv/bin/activate
	@python -m pip install -q poetry==1.8.5
	@poetry install

run: #enable virtualenv before make run
	@python web_scrapping.py 500

quality:
	@poetry run pre-commit run --all-files
