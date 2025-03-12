import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
parameters = {
    "lat": 37.456257,
    "lng": 126.705208,
    "formatted" : 0
}
sun_set_rise = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_set_rise.raise_for_status()
sun_info = (sun_set_rise.json()["results"]["sunrise"], sun_set_rise.json()["results"]["sunset"])
# print(sun_info)

sunrise = sun_info[0].split("T")[1].split(":")[0]
sunset = sun_info[1].split("T")[1].split(":")[0]
print((sunrise, sunset))