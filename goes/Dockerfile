FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev python3-tk build-essential

ADD . /code
WORKDIR /code
RUN pip3 install sunpy flask gunicorn requests bs4 drms suds-py3

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:8000"]
