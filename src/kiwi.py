import requests

def kiwiData(departureCity, destinationCity, date):

    url = "https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip"

    querystring = {
        "source": "City:" + departureCity,
        "destination": "City:" + destinationCity,
        "inboundDepartureDateStart": date + "T00:00:00",
        "currency": "dkk",
        "sortBy": "PRICE",
        "priceStart": "100",
        "priceEnd": "700"
    }

    headers = {
        "x-rapidapi-key": "31e7e22481msh53a25d3b7773558p1fc89bjsna63277f3b010",
        "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    flyRejser = response.json()

    return flyRejser