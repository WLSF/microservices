FROM python:3.6

MAINTAINER Willian Frantz willianluigii@gmail.com

ADD . /user

RUN pip install -r /user/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "user.src.main:app"]