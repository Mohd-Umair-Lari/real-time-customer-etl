# extract.py
import requests
import json

def extract_data():
    response=requests.get("https://fakestoreapi.com/products")
    if response.status_code==200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []
