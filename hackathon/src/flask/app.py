from flask import Flask, make_response, jsonify, request, json
import requests
from datetime import date

app = Flask(__name__)

API_KEY = "HgdRwVku2V1nD8yNuzaWPxco8RYB9HO8UpnJfIg6"

###
### API Responses
###


def get_response(status, data):
    return {
        "status": status,
        "data": data
    }

###
### Login API
###


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

###
### Retrieve User's Balanace API
###

@app.route("/balance/<custID>")
def get_balance(custID):
    API_ENDPOINT = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/accounts/view"
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }   
    body = {
        'custID': custID
    }

    response = requests.request("POST", API_ENDPOINT, headers=headers, data=json.dumps(body))
    return response.text


###
### Payment method
###

def _get_linked_accounts(accounts):
    # Assume there is only one linked account...?
    linked_account = None

    for account in accounts:
        if bool(account.get("linked", 'false')):
            linked_account = account

    return linked_account


def _call_update_API(custID, new_amount):
    API_ENDPOINT = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/accounts/update"
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        'custID': custID,
        'amount': new_amount
    }

    response = requests.request("POST", API_ENDPOINT, headers=headers, data=json.dumps(body))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def _call_add_transaction_API(**kwargs):
    API_ENDPOINT = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/add"
    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    # Do type casting because it is necessary apparently...?
    body = kwargs
    body["custID"] = int(body["custID"])
    body["payeeID"] = int(body["payeeID"])
    body["dateTime"] = str(body["dateTime"])
    body["amount"] = int(body["amount"])

    response = requests.request("POST", API_ENDPOINT, headers=headers, data=json.dumps(body))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/pay/<myID>/<payeeID>/<amount>")
@app.route("/pay/<myID>/<payeeID>/<amount>/<msg>")
def make_payment(myID, payeeID, amount, msg=""):
    my_accounts = json.loads(get_balance(int(myID)))
    my_linked_account = _get_linked_accounts(my_accounts)
    my_original_balance = my_linked_account.get("availableBal")
    my_new_balance = my_linked_account.get("availableBal") - int(amount)

    # Return response if there is not enough money
    if my_new_balance < 0:
        return get_response(400, "Not Enough Money")

    # To payee
    payee_accounts = json.loads(get_balance(int(payeeID)))
    payee_linked_account = _get_linked_accounts(payee_accounts)
    payee_new_balance = payee_linked_account.get("availableBal") + int(amount)

    response = _call_update_API(payeeID, payee_new_balance)
    if response.text != 'Successful transaction.':
        return get_response(500, "Unsuccessful transaction")

    response = _call_update_API(myID, my_new_balance)
    if response.text != 'Successful transaction.':
        # Revert to give the money back:
        _call_update_API(myID, my_original_balance)  
        return get_response(500, "Unsuccessful transaction")

    # Lastly, create a transaction for both parties
    today = date.today()
    _call_add_transaction_API(
        custID=myID,
        payeeID=payeeID,
        dateTime=today,
        amount=amount,
        expensesCat="",
        eGift=False,
        message=msg
    )

    _call_add_transaction_API(
        custID=myID,
        payeeID=payeeID,
        dateTime=today,
        amount=amount,
        expensesCat="",
        eGift=False,
        message=msg
    )

    transaction_data = {
        "custID": myID,
        "payeeID": payeeID,
        "dateTime": today,
        "amount": amount
    }

    return get_response(200, json.dumps(transaction_data))



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
