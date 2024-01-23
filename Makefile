export DJANGO_SUPERUSER_EMAIL ?= djangoadmin@example.com
export DJANGO_SUPERUSER_PASSWORD ?= admin

run:
	poetry run python manage.py runserver

superuser:
	poetry run python manage.py createsuperuser

reset:
	rm -rf db.sqlite3
	poetry run python manage.py migrate
	poetry run python manage.py createsuperuser --noinput

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

shell:
	poetry run python manage.py shell

install:
	pyenv local 3.12
	poetry config virtualenvs.prefer-active-python true
	poetry self add poetry-dotenv-plugin
	poetry install
