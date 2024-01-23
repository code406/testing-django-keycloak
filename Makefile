export DJANGO_SUPERUSER_EMAIL ?= djangoadmin@example.com
export DJANGO_SUPERUSER_PASSWORD ?= admin

run:
	poetry run python src/manage.py runserver

superuser:
	poetry run python src/manage.py createsuperuser

resetlocal:
	rm -rf src/db.sqlite3
	poetry run python src/manage.py migrate
	poetry run python src/manage.py createsuperuser --noinput

migrate:
	poetry run python src/manage.py migrate

makemigrations:
	poetry run python src/manage.py makemigrations

shell:
	poetry run python src/manage.py shell

install:
	pyenv local 3.12
	poetry config virtualenvs.prefer-active-python true
	poetry self add poetry-dotenv-plugin
	poetry install
