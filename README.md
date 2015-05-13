This Cookiecutter template setups a dev enviroment for my Django projects using Docker containers and django-compose.

## Containers
- data container - Data container for Postgres and redis data
- posgres - PostgreSQL
- redis - Redis
- nginx - Nginx for web access
- web - Python container running the Django project using Gunicorn. Installs requirements from requirements.txt
- pgweb - pgweb container for accessing the postgres database
- assets - asset building container running sass, compass, jshint, gulp, minification etc.

## Misc
- Docker setup with fig
- Django with PostgreSQL database
- PostgreSQL
- Redis
- Datacontainer for persistent data
- Nginx
- Gunicorn
- Sass
- Compass
- Compass breakpoint module
- Bootstrap
- jQuery
- Gulp with watch and livereload

## Commands
Run Django manage.py commands

	django-compose run --rm web ./manage.py migrate
	django-compose run --rm web ./manage.py syncdb

Creating a database (change DATABASE_NAME)

	django-compose run --rm postgres sh -c 'exec createdb -U postgres -h "$POSTGRES_PORT_5432_TCP_ADDR" DATABASE_NAME';
