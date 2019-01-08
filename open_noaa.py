import requests
import pandas as pd

r = requests.get(
    "http://0.0.0.0:8080/NOAA_report/get_data?day=20&month=4&year=2013")
try:
    data = pd.DataFrame(r.json())
    print(data)
except:
    print(r.json()["message"])
