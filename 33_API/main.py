# API (Application Programming Interface)
"""
Docstring for 33_API.main

An Applicaion Programming Interface (API) is a set 
of commands, functions, protocols and objects that
programmers can use to create software or interact 
with an external system.

API Endpoint ( URL )
API Request 

Response Codes ( Codes returned from API's )
1XX: Hold On 
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up 
5XX: I Screwed Up ( Server Screwed Up )

API Parameters (Give inputs when making API requests)

"""

import requests
from datetime import datetime
import time

MY_LAT = 33.602775
MY_LNG = 73.087291

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()    
    # print(data_iss)

    longitude_iss = float(data_iss["iss_position"]["longitude"])
    latitude_iss = float(data_iss["iss_position"]["latitude"])
    # print(longitude_iss, latitude_iss)

    if (MY_LAT-5)<=latitude_iss and (MY_LAT +5)>= latitude_iss and (MY_LNG - 5) <= longitude_iss and (MY_LNG + 5) >= longitude_iss:
        return True
    return False


def is_dark_outside():
    parameters = {
        "lat":MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid":"Asia/Karachi"
    }
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    # print(data_sun)

    sunrise = data_sun["results"]["sunrise"]
    sunset = data_sun["results"]["sunset"]
    # print(sunrise, sunset)

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    # print(sunrise_hour, sunset_hour)

    time_now = datetime.now()
    current_hour = int(time_now.hour)
    # print(time_now)
    # print(current_hour)

    if current_hour<=sunrise_hour or current_hour>=sunset_hour:
        return True
    return False


while True:
    time.sleep(60)
    
    if is_iss_overhead() and is_dark_outside():
        print("Sending Email")
    else:
        print("Ignore.")