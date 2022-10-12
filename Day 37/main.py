import requests
from datetime import datetime

USERNAME = "kaporli"
TOKEN = "xzehewvlabefjbfeufbrwqa"
GRAPH_ID = "graph1980"

pixella_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "xzehewvlabefjbfeufbrwqa",
    "username": "kaporli",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# Created user
# response = requests.post(url=pixella_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1980",
    "name": "Bootcamp Graph",
    "unit": "Days",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_formatted,
    "quantity": "1"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220607"

update_pixel_config = {
    "quantity": "2"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220607"

response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)