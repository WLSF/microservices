FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /blog-reply

RUN pip install -r /blog-reply/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "blog-reply.main:app"]