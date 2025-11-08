import requests
import json

def fly_scraperData():

    url = "https://fly-scraper.p.rapidapi.com/flights/search-roundtrip"

    querystring = {
        "originSkyId": "DK",
        "type": "roundtrip"
    }

    headers = {
        "x-rapidapi-key": "31e7e22481msh53a25d3b7773558p1fc89bjsna63277f3b010",
        "x-rapidapi-host": "fly-scraper.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(json.dumps(response.json(), indent=5))

    flyRejser = response.json()

    flyRejserClean = []

    for fly in flyRejser["data"]["everywhereDestination"]["results"]:

        pris = fly["content"]["flightQuotes"]["cheapest"]["price"]

        flyRejserClean.append({
           "pris": pris
        })
    
    print(flyRejserClean)

fly_scraperData()