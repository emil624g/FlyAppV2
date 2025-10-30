import requests
import json

url = "https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip"

querystring = {
    "source": "City:CPH,City:BLL,City:AAL,City:BLL,City:ODE",
    "destination": "Country:AL,Country:AD,Country:AM,Country:AT,Country:AZ,Country:BY,Country:BE,Country:BZ,Country:BA,Country:BG,Country:HR,Country:CY,Country:CZ,Country:DK,Country:EE,Country:FI,Country:FR,Country:GE,Country:DE,Country:GR,Country:HU,Country:IS,Country:IE,Country:IT,Country:KZ,Country:LV,Country:LI,Country:LT,Country:LU,Country:MT,Country:MD,Country:MC,Country:ME,Country:NL,Country:MK,Country:NO,Country:PL,Country:PT,Country:RO,Country:RU,Country:SM,Country:RS,Country:SK,Country:SI,Country:ES,Country:SE,Country:CH,Country:TR,Country:UA,Country:GB",
    "currency": "DKK",
    "sortBy": "PRICE",
    "priceEnd": "4000",
    "transportTypes": "FLIGHT",
    "sortOrder": "ASCENDING",
    "limit": "50"
}

headers = {
    "x-rapidapi-key": "31e7e22481msh53a25d3b7773558p1fc89bjsna63277f3b010",
    "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(json.dumps(response.json(), indent=4))

flyResjer = response.json()

flyRejserClean = []

for fly in flyResjer["itineraries"]:

    pris = fly["price"]["amount"]
    fra = fly["outbound"]["sectorSegments"][0]["segment"]["source"]["station"]["name"]
    til = fly["outbound"]["sectorSegments"][0]["segment"]["destination"]["station"]["city"]["legacyId"]
    url = fly["bookingOptions"]["edges"][0]["node"]["bookingUrl"]
    udrejseAfgang = fly["outbound"]["sectorSegments"][0]["segment"]["source"]["localTime"]
    udrejseAnkomst = fly["outbound"]["sectorSegments"][0]["segment"]["destination"]["localTime"]
    hjemrejseAfgang = fly["inbound"]["sectorSegments"][0]["segment"]["source"]["localTime"]
    hjemrejseAnkomst = fly["inbound"]["sectorSegments"][0]["segment"]["destination"]["localTime"]

    if any(entry["fra"] == fra and entry["til"] == til for entry in flyRejserClean):
        continue

    flyRejserClean.append({
        "til": til,
        "fra": fra,
        "pris": pris,
        "url": "https://kiwi.com" + url,
        "udrejseAfgang": udrejseAfgang,
        "udrejseAnkomst": udrejseAnkomst,
        "hjemrejseAfgang": hjemrejseAfgang,
        "hjemrejseAnkomst": hjemrejseAnkomst
    })

print(json.dumps(flyRejserClean, indent=4, ensure_ascii=False))