This Cookiecutter template setups a dev enviroment for my Django projects using Docker containers and docker-compose.

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

## Generate Django secret key
A Django secret key can be generated with the following command:

    python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'

## Additinal info
Check the generated README.md for more info and commands.
