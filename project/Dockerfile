# pull official base image
FROM python:3.10.6

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN python -m pip install --upgrade pip
COPY requirements /usr/src/app/requirements
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements/dev.txt

# add app
COPY . .