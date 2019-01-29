import requests
import pandas as pd

r = requests.get("http://0.0.0.0:5000/rstn/get_data?day=25&month=4&year=2000")
try:
    data = pd.DataFrame(r.json())
    print(data)
except:
    print(r.json()["message"])
