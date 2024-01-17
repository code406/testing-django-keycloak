run:
	poetry run python src/manage.py runserver

superuser:
	poetry run python src/manage.py createsuperuser

migrate:
	poetry run python src/manage.py migrate

makemigrations:
	poetry run python src/manage.py makemigrations

shell:
	poetry run python src/manage.py shell
