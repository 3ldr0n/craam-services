FROM python:3.7-slim

WORKDIR /goes_service
ADD . /goes_service

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
