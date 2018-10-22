FROM python:3.6

ADD . /reply

RUN pip install -r /reply/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "reply.src.main:app"]