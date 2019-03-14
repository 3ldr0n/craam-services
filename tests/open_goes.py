import requests
import pandas as pd


# Time format: YYYY-MM-DD HH:MM:SS

r = requests.get(
    "http://0.0.0.0:5000/goes/get_data?begin=2015-10-31 12:40:00&end=2015-10-31 12:50:00")
try:
    data = pd.DataFrame(r.json())
    print(data)
except:
    print(r.json()["message"])
