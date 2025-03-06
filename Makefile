PIP := venv/scripts/pip
PYTHON3 := venv/scripts/python

clear:
	rd -r venv

venv:
	python -m venv venv

requirements:
	${PIP} install -r requirements.txt

migrate:
	${PYTHON3} manage.py makemigrations
	${PYTHON3} manage.py migrate

run:
	${PYTHON3} manage.py runserver