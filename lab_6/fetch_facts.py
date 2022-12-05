import requests

def get_dog_fact():
    r = requests.get('https://dog-api.kinduff.com/api/facts')
    if r.status_code == 200:
        r = r.json()['facts'][0]
        return r
    return 'opsy'

def get_cat_fact():
    return 'Cat facts now are not avalible error 500'
