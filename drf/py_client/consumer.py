import  requests

endpoint='http://127.0.0.1:8000/api/'

# resp=requests.get(endpoint)
# print(resp.json()['message'])

resp=requests.get(endpoint,params={'abc':123},json={"query":"hello world"})
print(resp.json()['message'])