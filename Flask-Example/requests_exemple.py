# encode=utf-8

import requests
import json


# GET
def request_viacep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())


API_URL = "http://api.positionstack.com/v1/reverse"
API_KEY = "12789d781f9cc6ad750be832db"


# GET
def request_address_by_coords(latitude, longitude):
    query = f"{latitude},{longitude}"
    params = dict(access_key=API_KEY, query=query, limit=1)

    response = requests.get(API_URL, params=params)
    print(response.status_code)
    print(response.text)


# POST
# def


request_viacep(89036005)
