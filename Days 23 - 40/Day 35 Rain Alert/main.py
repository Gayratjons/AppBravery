import requests
API_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "a9328147ff7014c1f567d0b662182359"
print(api_key)
weather_params = {
    "lat":37.456257,
    "lon":126.705208,
    'appid': api_key
}

data = requests.get(API_Endpoint, params=weather_params)
data.raise_for_status()
data = data.json()["list"] 
print(type(data))

# hourly_data = [data["list"][0]["weather"][0]["id"]]
hourly_notation = [("Bring an umbrella", data[i]["weather"][0]["id"]) if data[i]["weather"][0]["id"] < 700 else ("No need for an Umbrella", data[i]["weather"][0]["id"]) for i in range(4)]


print(hourly_notation)


 