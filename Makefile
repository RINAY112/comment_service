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

build:
	docker build -t comment_service .

run:
	docker run -p 8000:8000 comment_service

stop:
	docker stop $(docker ps -q --filter ancestor=comment_service)

kill:
	docker kill $(docker ps -q --filter ancestor=comment_service)