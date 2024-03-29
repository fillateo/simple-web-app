FROM python:3.11

RUN apt-get -qq update
RUN pip install --upgrade pip && pip install pip-tools
RUN apt-get install -y --no-install-recommends g++ docker.io

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn wsgi:app -b  0.0.0.0:5000 --workers=1 --preload
