import requests
import json

# Load JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)


# Define the URL for the POST request
url = 'http://localhost:3001/signup'

# Send the POST request with the JSON data
response = requests.post(url, json=data)

# Print the response from the server
print(response.status_code, response.content)
