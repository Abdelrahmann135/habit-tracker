import requests
from datetime import *
TOKEN = "abdelrahmanalaa135@13"
USERNAME = "abdelrahman13"
ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# create new user
user_par = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_par)
# print(response.text)

# create new graph
graph_par = {
    "id": ID,
    "name": "habit tracker",
    "unit": "calory",
    "type": "float",
    "color": "sora",
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_par, headers=HEADERS)
# print(response.text)

# post a pixel
post_endpoint = f"{GRAPH_ENDPOINT}/{ID}"
date = datetime.now().strftime("%Y%m%d")
post_par = {
    "date": date,
    "quantity": "550.5"
}
# response = requests.post(url=post_endpoint, json=post_par, headers=HEADERS)
# print(response.text)

# update a pixel
wanted_date_to_update = date
update_endpoint = f"{post_endpoint}/{wanted_date_to_update}"
update_par = {
    "quantity": "500.6"
}
# response = requests.put(url=update_endpoint, json=update_par, headers=HEADERS)
# print(response.text)

# delete a pixel
wanted_date_to_delete = date
delete_endpoint = f"{post_endpoint}/{wanted_date_to_delete}"
# response = requests.delete(url=delete_endpoint, headers=HEADERS)
# print(response.text)
