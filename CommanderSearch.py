import pandas as pd
from API.EDHRec import getData

def search(commander):


    df_collection = pd.read_csv(r'DataOutput\ScryfallData.csv', sep=';')
    df_commander = getData(commander)
    
    df = df_commander
    merge = pd.merge(df, df_collection, on=['name'], how='inner')
    print(merge)
    #merge.to_excel(r'DataOutput\SearchResults.xlsx')

search('grand-arbiter-augustin-iv')
