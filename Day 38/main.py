
import requests
from datetime import datetime
APP_ID = "efb0ae4b"
API_KEY = "032ca44b1374fe8ae393b49a8b8e4be4"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

headers_sheety = {
    "Authorization": "Basic a2Fwb3JsaTpMaWZlMTk4MDs="
}


nutritionix_config = {
    "query": input("What did you do for exercise? "),
    "gender": input("Are you male or female? "),
    "weight_kg": input("How much do you weight in kg? "),
    "height_cm": input("How tall are you in cm? "),
    "age": input("How old are you? ")
}

# response = requests.post(url=nutritionix_endpoint, json=exercise_config, headers=headers)
# # print(response.text)

response = requests.post(nutritionix_endpoint, json=nutritionix_config, headers=headers)
result = response.json()

sheety_endpoint = "https://api.sheety.co/acd67aa04e45dd48add0b82a48a99f03/workoutTracking/workouts"
# sheety_endpoint_put = f"{sheety_endpoint}/4"

# today = datetime.now()
# today_formatted = today.strftime("%d/%m/%Y")
#
# time = datetime.now()
# time_formatted = time.strftime("%H:%M:%S")
#
# workout = {
#     "workouts": {
#         "a": today_formatted,
#         "b": time_formatted,
#         "c": exercise_config["query"],
#         "e": "130"
#     }
# }
#
# response1 = requests.post(url=sheety_endpoint_put, json=workout)
# print(response1.text)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers_sheety)

    print(sheet_response.text)