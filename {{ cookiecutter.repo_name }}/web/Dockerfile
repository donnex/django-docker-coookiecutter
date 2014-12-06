FROM python:2.7

WORKDIR /wwwroot

COPY requirements.txt /wwwroot/

RUN pip install -r requirements.txt

RUN rm requirements.txt

RUN useradd -s /bin/bash -u 3000 -M {{cookiecutter.repo_name}}_user

USER {{cookiecutter.repo_name}}_user

COPY {{cookiecutter.repo_name}} /wwwroot/

ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["gunicorn", "--log-file=-", "--workers 4", "--name {{cookiecutter.repo_name}}_gunicorn", "-b 0.0.0.0:8000", "{{cookiecutter.repo_name}}.wsgi:application"]
