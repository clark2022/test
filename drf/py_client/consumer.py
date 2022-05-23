import  requests

endpoint='http://127.0.0.1:8000/api/'

resp=requests.get(endpoint)
print(resp.json()['message'])