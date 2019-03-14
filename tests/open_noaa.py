import requests
import pandas as pd

r = requests.get(
    "http://0.0.0.0:5000/noaa_report/get_data?day=20&month=4&year=2013")
try:
    data = pd.DataFrame(r.json())
    print(data)
except:
    print(r.json()["message"])
