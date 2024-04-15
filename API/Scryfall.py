import requests 
import json
import pandas as pd



def getData(card_name, set_code):
    r = requests.get('https://api.scryfall.com/cards/named?exact='+card_name+'&set_name='+set_code)
    data = r.text

    results = json.loads(data)
    results = pd.json_normalize(results)

    return results