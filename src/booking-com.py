import requests
import json

from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

destinations = ["LON.AIRPORT", "PAR.AIRPORT", "NYC.AIRPORT", "DXB.AIRPORT"]

def fly_scraperData():

    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"

    for toId in destinations:
        querystring = {
            "fromId": "AAL.AIRPORT",
            "toId": toId,
            "departDate": date
        }

    headers = {
        "x-rapidapi-key": "31e7e22481msh53a25d3b7773558p1fc89bjsna63277f3b010",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(json.dumps(response.json(), indent=4))

fly_scraperData()