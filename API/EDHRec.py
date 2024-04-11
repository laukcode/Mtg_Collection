import requests 
import json
import pandas as pd

card = 'the-ur-dragon'
card = card.replace(' ', '-')


def getData(card_name):
    r = requests.get('https://json.edhrec.com/pages/commanders/'+card_name+'.json')
    data = r.text

    results = json.loads(data)
    results = pd.json_normalize(results,'cardlist')

    return results
