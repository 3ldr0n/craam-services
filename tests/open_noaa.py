import requests
import pandas as pd

r = requests.get(
    "http://0.0.0.0:8080/noaa_report/get_data/2013/4/20")

try:
    data = pd.DataFrame(r.json())
    print(data)
except Exception as e:
    print(e)
    print(r.json()["message"])
