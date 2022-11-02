FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /llatrofproject/llatrof

ADD . /llatrofproject/docker-server

WORKDIR /llatrofproject/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80
