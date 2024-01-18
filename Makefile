export DJANGO_SUPERUSER_USERNAME ?= admin
export DJANGO_SUPERUSER_PASSWORD ?= admin
export DJANGO_SUPERUSER_EMAIL ?=

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
