FROM python:3.7-slim

WORKDIR /rstn_service
COPY . /rstn_service

RUN pip install flask gunicorn getrstn

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
