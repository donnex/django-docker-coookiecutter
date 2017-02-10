# django-docker-coookiecutter

[Cookiecutter](https://github.com/audreyr/cookiecutter) project template that setups a dev enviroment for Django projects using Docker containers with docker-compose.

This setup is currently only intended to be used in dev, not production.

## Containers

- data container - Data container for Postgres and redis data
- posgres - PostgreSQL
- redis - Redis
- nginx - Nginx for web access
- django - Python container running the Django project using Gunicorn. Installs requirements from requirements.txt
- pgweb - pgweb container for accessing the postgres database
- assets - asset building container running sass, compass, jshint, gulp, minification etc.

## Misc

- Docker setup with docker-compose
- Django with PostgreSQL database
- PostgreSQL
- Redis
- Data volume for persistent data (posgres + redis)
- Nginx
- Gunicorn
- Sass
- Compass
- Compass breakpoint module
- Bootstrap
- jQuery
- Gulp with watch and livereload

## How to use

First install cookiecutter, probably:

    pip install cookiecutter

Run cookiecutter to generate a new project folder, complete with project folders and docker-compose setup:

    cookiecutter https://github.com/donnex/django-docker-coookiecutter

Answer the questions from cookiecutter. The project output folder is repo_name in the cookiecutter questions.

cd into the new repo_name folder and run:

    docker-compose up

As long as you've added your virtual hosts to the host file and run the nginx-proxy container you should be able to browse to your virtual host in your browser.

## Generate Django secret key

A Django secret key can be generated with the following command:

    python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'

## Nginx proxy

Run the nginx-proxy on port 80 to use the virtual hosts. I'm adding my virtual hosts to /etc/hosts.

    docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock --name nginx-proxy jwilder/nginx-proxy

## Additinal info

Check the generated README.md for more info and commands.
