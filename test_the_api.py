import requests

query = {'num1':'4', 'num2':'10'}
response = requests.get('http://localhost:7000/sum', params=query)
print(response.json())