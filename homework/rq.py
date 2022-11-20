import requests

def get_req(num_to_request: int):
    r = requests.get('http://127.0.0.1:5000/num/{}'.format(num_to_request))
    return r