# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# # set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install django
RUN pip install prometheus-client

# copy project
COPY . .
CMD ["python","manage.py", "runserver"]
