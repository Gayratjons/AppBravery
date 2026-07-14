import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
parameters = {
    "lat": 37.456257,
    "lng": 126.705208,
    "formatted": 0
}

def get_iss_pos():
    pass
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return {"lat": float(data["iss_position"]["latitude"]), "lng": float(data["iss_position"]["longitude"])}

sun_set_rise = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_set_rise.raise_for_status()
sun_info = (sun_set_rise.json()["results"]["sunrise"], sun_set_rise.json()["results"]["sunset"])
# print(sun_info)

sunrise = int(sun_info[0].split("T")[1].split(":")[0])
sunset = int(sun_info[1].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
print(get_iss_pos())
hour_now = datetime.now().hour
print(hour_now)


lat_check = False
lng_check = False

if hour_now > sunset:
    if get_iss_pos()["lat"] + 5 >= parameters["lat"] and get_iss_pos()["lat"] - 5 <= parameters["lat"]:
        lat_check = True
    if get_iss_pos()["lng"] + 5 >= parameters["lng"] and get_iss_pos()["lng"] - 5 <= parameters["lng"]:
        lng_check = True
if lat_check and lng_check:
    print("look up")
