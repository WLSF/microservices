FROM python:3.7-alpine

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /blog-user

RUN pip install -r /blog-user/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "blog-user.main:app"]