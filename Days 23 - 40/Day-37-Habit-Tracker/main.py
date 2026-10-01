import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jb0w46b3pz6tmad5udqoz",
    "username" : "axilles",
    "agreeTermsOfService": "yes",
    "notMinor": "yes" 
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{user_params["username"]}/graphs"

graph_config = {
    "id": "graph-2",
    "name" : "Book Page Counter",
    "unit": "Pages",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN" : user_params["token"]
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


addpixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"

# addpixel_config = {
#     "date": "20260721",
#     "quantity": "7"
# }

today = datetime(year=2026, month=7, day=20)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}
# response = requests.post(url=addpixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)


updatepixel_config = {
    "quantity": "9"
}
update_endpoint = f"{addpixel_endpoint}/{pixel_data['date']}"
# response = requests.put(url=update_endpoint, json=updatepixel_config, headers=headers)
# print(response)



response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
