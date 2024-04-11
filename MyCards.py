import pandas as pd
from API.Scryfall import getData

def CardLookup():

    df = pd.read_csv(r'Collection\my_cards.csv', sep=',', skiprows=1)

    name_list = df['Card Name'].tolist()
    set_list = df['Set Code'].tolist()

    for name in name_list:
        i = name_list.index(name)
        set_code = set_list[i]
        row = getData(name, set_code)
        if i == 0:
            df = row
        else: 
            df = pd.concat([df, row])

    return df

CardLookup().to_excel('MyCollection.xlsx', index=False)
