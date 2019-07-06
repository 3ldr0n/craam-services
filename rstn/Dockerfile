FROM python:3.7-slim

ADD . /rstn

WORKDIR /rstn

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
