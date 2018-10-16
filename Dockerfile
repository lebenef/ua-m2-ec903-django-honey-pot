FROM python:3.6-alpine

RUN python -m venv /venv

RUN source /venv/bin/activate

RUN pip install Django

RUN mkdir /code/

WORKDIR /code/

RUN git clone https://github.com/lebenef/ua-m2-ec903-django-honey-pot.git

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=project.settings.deploy

ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=/code/ua-m2-ec903-django-honey-pot/project/project/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
