import requests

#from nicegui import ui

#ui.input('Text input')

#ui.run()

# Define the payload
payload = {"data": "Dette er en test"}

# Make the POST request
response = requests.post("http://localhost:8000/encode", json=payload)

# Check the response status code
if response.status_code == 200:
    # The request was successful
    print("The data was encoded successfully!")
    #encoded_data = response.json()["data"]
    encoded_data = response.content.decode('utf-8')

    # Remove the unwanted characters
    clean_encoded_data = encoded_data[1:-1]
    

    # Do something with the encoded data
    print(clean_encoded_data)
else:
    # The request failed
    print("An error occurred while encoding the data:", response.status_code)