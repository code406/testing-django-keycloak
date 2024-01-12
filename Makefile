run:
	poetry run python src/manage.py runserver

superuser:
	poetry run python src/manage.py createsuperuser
