FROM python:3.7-slim

RUN pip install sunpy flask gunicorn requests bs4 drms suds-py3

WORKDIR /goes_service
COPY . /goes_service

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
