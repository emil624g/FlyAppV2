import requests
import json

from kiwi import kiwiData

def aviation():

    params = {
        'dep_iata': 'CPH',
        'flight_status': 'scheduled',
        'access_key': '55994c5ac2703b2292a22615efd81128'
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    flyRejserClean = []

    for fly in api_response['data']:

        fra = fly['departure']['iata']
        til = fly['arrival']['iata']
        dato = fly['flight_date']

        flyRejserClean.append(kiwiData(fra, til, dato))

    return json.dumps(flyRejserClean, indent=4, ensure_ascii=False)