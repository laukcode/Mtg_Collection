import pandas as pd
import time
import requests
from API.Scryfall import getData


def ReplaceAll(name):
    replaced = [' ',',',"'",'/']
    for letter in replaced:
        if letter == ' ':
            name = name.replace(letter, '_')
        else:
            name = name.replace(letter, '')
    return name

def CardLookup():

    df = pd.read_csv(r'DataInput\my_cards.csv', sep=',', skiprows=1)
    #df = pd.read_csv(r'DataInput\test_card.csv', sep=',', skiprows=1)

    name_list = df['Card Name'].tolist()
    set_list = df['Set Code'].tolist()

    for name in name_list:
        i = name_list.index(name)
        set_code = set_list[i]
        row = getData(name, set_code)
        
        # Download Image
        if 'image_uris.normal' in row:
            img_url = row['image_uris.normal'][0]
        else: img_url = 'https://cards.scryfall.io/normal/front/e/8/e88ae6bf-9c58-4543-ba66-19ea41d01e9b.jpg?1576384102'

        folder_path = 'DataOutput\\CardImages\\'
        file_path = folder_path + set_code + '_' + ReplaceAll(name) + '.jpg'

        try:
            img = requests.get(img_url).content
            with open(file_path, 'wb') as handler:
                handler.write(img)
        except:
            print('Image not found for: ' + set_code + ' ' + name)

        # Create synced table
        if i == 0:
            df = row
        else: 
            df = pd.concat([df, row])
        print('Scryfall data imported for Card: ' + name)
        time.sleep(0.1)
    
    df.to_csv(r'DataOutput\ScryfallData.csv', sep=';', index=False)
    
    return df

CardLookup()