import pandas as pd
from MyCards import CardLookup
from API.EDHRec import getData

def search(commander):


    df_collection = CardLookup()
    df_commander = getData(commander)
    
    df = df_commander
    merge = pd.merge(df, df_collection, on=['name'], how='inner')
    print(merge)
    merge.to_excel('SearchResults.xlsx')

search('intet-the-dreamer')
