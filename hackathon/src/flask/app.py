from flask import Flask, make_response, jsonify, request, json
import requests

app = Flask(__name__)

API_KEY = "HgdRwVku2V1nD8yNuzaWPxco8RYB9HO8UpnJfIg6"

@app.route("/login", methods=["POST"])
def login():
    if not (request.method == "POST"):
        return 400

    login_data = request.json
    username = login_data['username']
    password = login_data['password']

    url = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login"

    payload = {
        "username" : username, 
        "password" : password
    }

    headers = {
    'x-api-key': API_KEY,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.text


@app.route("/tranHist/<custID>")
def view_transaction_history(custID):

    url = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/view"

    payload = {
        "custID" : custID
    }

    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    response = json.loads(response.text)
    return jsonify(response)
    

if __name__=='__main__':
    app.run(port=5002, debug=True)
    app.run()
    