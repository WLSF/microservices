FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /post

RUN pip install -r /post/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "post.src.main:app"]