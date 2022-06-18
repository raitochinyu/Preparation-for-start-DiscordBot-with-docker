FROM python:3.9.5
WORKDIR /raitochinyu/

RUN apt-get update
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

COPY .env /.env
COPY /cogs /raitochinyu/cogs
COPY /config /raitochinyu/config
COPY /notice /raitochinyu/notice
COPY requirements.txt /raitochinyu/
RUN pip install --upgrade pip
RUN pip install -r /raitochinyu/requirements.txt

COPY main.py /raitochinyu/
