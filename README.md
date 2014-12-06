This Cookiecutter template setups a dev enviroment for my Django projects using Docker containers and fig.

## Containers
- data container - Data container for Postgres and redis data
- posgres - PostgreSQL
- redis - Redis
- nginx - Nginx for web access
- web - Python container running the Django project using Gunicorn. Installs requirements from requirements.txt
- pgweb - pgweb container for accessing the postgres database
- assets - asset building container running sass and compass

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

## Commands
Run Django manage.py commands

	fig run --rm web ./manage.py migrate
	fig run --rm web ./manage.py syncdb
	
Creating a database

	fig run --rm postgres sh -c 'exec createdb -U postgres -h "$POSTGRES_PORT_5432_TCP_ADDR" DATABASE_NAME';