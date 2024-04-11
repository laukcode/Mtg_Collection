import requests 
import json
import pandas as pd



def getData(card_name, set_code):
    r = requests.get('https://api.scryfall.com/cards/search?order=cmc&q='+card_name+'+set%3A'+set_code)
    data = r.text

    results = json.loads(data)
    results = pd.json_normalize(results, 'data')

    return results