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


"""

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()
data = response.json()    
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(longitude, latitude)