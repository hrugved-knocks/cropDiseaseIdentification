import requests
import json
import base64



endpoint = 'https://api.vize.ai/v2/classify/'

headers = {
    'Authorization': "Token 4014e861e03335c62c8308e9d61fd3a4e54af5e8",
    'Content-Type': 'application/json'
}

with open('test1.jpeg', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {
    'task_id': '1e711d02-9420-4b58-b4d6-0a5d8472091d',
    'records': [ {"_base64": encoded_string } ]
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))

responseJson = response.json()

responseJson= response.json()
print(responseJson)
print(type(responseJson['records'][0]['best_label']))
for i in responseJson['records'][0]['best_label'].values():
    print(i)
#print(json.dumps(response.json(), indent=4))
resultFu = [ ]
resultFu.append(responseJson['records'][0]['best_label']['name'])
resultFu.append(responseJson['records'][0]['best_label']['prob'])

print(resultFu)

'''

# First way to load base64
with open('test.jpg', "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Second way to load base64 data with opencv
#image = cv2.imread(__IMAGE_PATH__) # this will return image in BGR
#retval, buffer = cv2.imencode('.jpg', image)
#encoded_string = base64.b64encode(buffer).decode('utf-8')

data = {
    'records': [ {"_base64": encoded_string } ],
    'task_id':'1e711d02-9420-4b58-b4d6-0a5d8472091d'
    }

response = requests.post(url, headers=headers, data=json.dumps(data))
if response.raise_for_status():
    print(json.dumps(response.json(), indent=2))
else:
    print('Error posting API: ' + response.text)
    ;'''