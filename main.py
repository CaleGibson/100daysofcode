import requests
from datetime import datetime
USER = "cale"
TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"
pix_params = {
    "token": TOKEN ,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=pixela_endpoint, json=pix_params)
#print(response.text)

today = datetime.now()
new_today = today.strftime("%Y%m%d")
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_param = {
    "id": "myhabit0",
    "name": "Miles Ran",
    "unit": "float",
    "type": "int",
    "color": "ajisai"
}
headers = {
     "X-USER-TOKEN": TOKEN
}

#post a pixle
pixle_end = f"{pixela_endpoint}/{USER}/graphs/myhabit0"
pixle_json = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "30",
}

pix_up_json = {
    "quantity": "1"
}
#response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
#print(response.text)

#response = requests.post(url=pixle_end, json=pixle_json, headers=headers)
#print(response.text)

#pixel_update_end = f"{pixela_endpoint}/{USER}/graphs/myhabit0/{new_today}"
#response = requests.put(url=pixel_update_end, headers=headers, json=pix_up_json)
#print(response.text)

pixel_delete = f"{pixela_endpoint}/{USER}/graphs/myhabit0/{new_today}"
response = requests.delete(url=pixel_delete, headers=headers)
print(response.text)