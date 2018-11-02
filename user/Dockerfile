FROM python:3.6

COPY requirements.txt /user/
RUN pip install -r /user/requirements.txt
COPY . /user/

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "user.src.main:app"]