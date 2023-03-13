import requests

url = 'http://localhost:5000/input'
payload = {'client': 'Fred', 'data': 'I will buy all the doge coins in this world today'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)
print(response.content)
print("")

# Send a GET request to read the blockchain
response = requests.get('http://localhost:5000/blocks')
print(response.content) # Print the response in JSON format
print("")
print("")
url = 'http://localhost:5000/input'
payload = {'client': 'Fred', 'data': 'doge coin is losing money now! sell all!'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)
print(response.content)
print("")

# Send a GET request to read the blockchain
response = requests.get('http://localhost:5000/blocks')
print(response.content) # Print the response in JSON format
print("")
# Send a GET request to read the blockchain
response = requests.get('http://localhost:5000/blocks')
print(response.content) # Print the response in JSON format