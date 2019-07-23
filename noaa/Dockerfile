FROM python:3.7

ADD . /noaa

WORKDIR /noaa

# Fetch NOAA report files
RUN cd reports && python grab-reports.py

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
