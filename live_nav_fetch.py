import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_data = data["data"]

df = pd.DataFrame(nav_data)

df.to_csv("hdfc_top100_nav.csv", index=False)

print("NAV data saved successfully!")