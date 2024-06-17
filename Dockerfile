FROM python:3.12.4-alpine3.20
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /tasks

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt


COPY tasks ./tasks

ENV HOME=/tasks
RUN mkdir $HOME/staticfiles
WORKDIR /tasks/tasks

RUN python manage.py collectstatic --no-input

WORKDIR /tasks
EXPOSE 8000

RUN adduser -D myuser
USER myuser
