FROM python:3.8.0-alpine
MAINTAINER Viacheslav Reshetylo

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN mkdir -p /usr/vehicle_api_django
WORKDIR /usr/vehicle_api_django
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "crontab", "add"]
CMD ["python", "manage.py", "runserver"]