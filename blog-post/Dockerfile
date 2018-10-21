FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /blog-post

RUN pip install -r /blog-post/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "blog-post.main:app"]