import requests
from datetime import datetime
MY_LAT = 50.879845
MY_LONG = 4.700518

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_pos = (longitude, latitude)
#
# print(iss_pos)

parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sp = sunrise.split("T")

time_now = datetime.now()
# print(time_now)
print(sp[1])