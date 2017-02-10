# {{cookiecutter.project_name}}

## PostgreSQL

**postgres password**: {{cookiecutter.postgres_password}}

**database url**: postgres://postgres:{{cookiecutter.postgres_password}}@postgres/{{cookiecutter.repo_name}}?sslmode=disable

## Hosts

**Django**: {{cookiecutter.virtual_host}}
**Pgweb**: pgweb.{{cookiecutter.virtual_host}}

## Commands
Creating the database:

    docker-compose run --rm postgres sh -c 'exec createdb -U postgres -h "$POSTGRES_PORT_5432_TCP_ADDR" {{cookiecutter.repo_name}}';

Run Django manage.py commands:

    docker-compose run --rm django ./manage.py help
    docker-compose run --rm django ./manage.py migrate
    docker-compose run --rm django ./manage.py createsuperuser
    docker-compose run --rm django ./manage.py collectstatic
    docker-compose run --rm django ./manage.py startapp APP_NAME
