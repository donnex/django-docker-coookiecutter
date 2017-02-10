import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{{cookiecutter.repo_name}}.settings')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
