# transform.py
import pandas as pd
import re

def transform_data(raw_data):
    df=pd.json_normalize(raw_data)
    df['title']=df['title'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
    df['price']=df['price'].astype(float)
    df['category']=df['category'].str.title()
    return df[['id', 'title', 'price', 'category', 'description']]
