FROM python:3.6

ADD . /post

RUN pip install -r /post/requirements.txt

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "post.src.main:app"]