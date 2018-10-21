FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /reply

RUN pip install -r /reply/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "reply.main:app"]