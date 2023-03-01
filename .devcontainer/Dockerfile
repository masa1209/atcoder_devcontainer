FROM python:3.8.2-buster

ENV PYTHONUNBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code
ENV DEBCONF_NOWARNINGS=yes

RUN mkdir /code
WORKDIR /code
COPY .devcontainer/requirements.txt .
RUN apt update
RUN apt-get install -y nodejs
RUN apt install -y nodejs npm 
RUN npm install -g atcoder-cli
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
