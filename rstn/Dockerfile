FROM python:3.7-slim

RUN pip install flask gunicorn getrstn

WORKDIR /rstn_service
ADD . /rstn_service

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
