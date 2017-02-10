FROM python:3.5

ARG requirements_file

WORKDIR /wwwroot

COPY {{cookiecutter.repo_name}} /wwwroot

RUN pip install -r ${requirements_file:-requirements/prod.txt}

RUN useradd -s /bin/bash -u 3000 -M {{cookiecutter.repo_name}}_user

USER {{cookiecutter.repo_name}}_user

ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["gunicorn", "--log-file=-", "--workers 4", "--name {{cookiecutter.repo_name}}_gunicorn", "-b 0.0.0.0:8000", "{{cookiecutter.repo_name}}.wsgi:application"]
