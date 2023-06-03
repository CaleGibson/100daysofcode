import requests
import os
from datetime import datetime
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NAT_EX_LINK = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_LINK = os.environ["SHEETY_LINK"]
params = {
    "query": input("What did you do today? "),
    "gender": "male",
    "weight_kg": "83",
    "height_cm": "175"
}
header= {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
sheety_header = os.environ["BEARER_TOKEN"]
response = requests.post(url=NAT_EX_LINK, json=params, headers=header)
data = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")
print(current_time)
for all in data["exercises"]:
    sheet_input = {
    "workout":{
        "date": current_date,
        "time": current_time,
        "exercise": all["name"],
        "duration": all["duration_min"],
        "calories": all["nf_calories"],
        }
    }
    response = requests.post(SHEETY_LINK, json=sheet_input, headers=sheety_header)
    print(response.text)
