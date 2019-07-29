import requests
import pandas as pd

r = requests.get("http://0.0.0.0:8080/rstn/get_data/2002/4/9/sagamore hill")
try:
    data = pd.DataFrame(r.json())
    print(data)
except Exception as e:
    print(e)
    print(r.json()["message"])
