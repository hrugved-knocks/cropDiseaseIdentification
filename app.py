from flask import Flask,render_template,jsonify,request

import requests
import json
import os
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/getClassification', methods=['POST'])
def getClassification():

    #GLOBALS
    UPLOAD_FOLDER = os.path.basename('static')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    file = request.files['image']
    f=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)



    '''
    name = request.data
    my_json = name.decode('utf8').replace("'", '"')
    s = json.dumps(my_json, indent=4, sort_keys=True)
    data = s.split('=')
    print(data[1][:-1])
    '''


    endpoint = 'https://api.vize.ai/v2/classify/'
    headers = {
        'Authorization': "Token 4014e861e03335c62c8308e9d61fd3a4e54af5e8",
        'Content-Type': 'application/json'
    }
    with open(f, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    data = {
        'task_id': '1e711d02-9420-4b58-b4d6-0a5d8472091d',
        'records': [ {"_base64": encoded_string } ]
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    responseJson = response.json()

    responseJson= response.json()
    print(responseJson)
    # print(type(responseJson['records'][0]['best_label']))
    # for i in responseJson['records'][0]['best_label'].values():
        # print(i)
    #print(json.dumps(response.json(), indent=4))
    resultFu = [ ]
    resultFu.append(responseJson['records'][0]['best_label']['name'])
    resultFu.append(responseJson['records'][0]['best_label']['prob'])
   
    
    return render_template('result.html',result=resultFu,imagePath=f)

