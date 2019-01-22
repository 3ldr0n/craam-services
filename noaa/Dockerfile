FROM python:3.7-slim

WORKDIR /noaa_service
COPY . /noaa_service

RUN pip install flask gunicorn noaareport

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
