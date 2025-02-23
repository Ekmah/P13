# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
#CMD ["gunicorn", "oc_lettings_site.wsgi", "--bind 0.0.0.0:$PORT"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
#CMD python3 manage.py runserver 0.0.0.0:$PORT
