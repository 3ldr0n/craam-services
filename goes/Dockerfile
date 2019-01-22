FROM python:3.7-slim

WORKDIR /goes_service
COPY . /goes_service

RUN pip install sunpy flask gunicorn requests bs4 drms suds-py3

EXPOSE 80

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]
