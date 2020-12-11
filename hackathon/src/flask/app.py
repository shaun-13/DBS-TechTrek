from flask import Flask, make_response
import requests

app = Flask(__name__)

API_KEY = "HgdRwVku2V1nD8yNuzaWPxco8RYB9HO8UpnJfIg6"

# @app.route("/findPlaceFromText/<input_location>")
# def findPlaceFromText(input_location):
#     API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={apiKey}&input={input_location}&inputtype={inputtype}&fields={fields}"
#     inputtype = "textquery"
#     fields = "geometry"
#     url_to_send = API_ENDPOINT.format(apiKey = API_KEY, input_location = input_location, inputtype = inputtype, fields = fields)
#     payload = {}
#     headers= {}
#     response = requests.request("GET", url_to_send, headers=headers, data = payload)
#     response = make_response(response.json())
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response

# @app.route("/findPlaceFromUserText/<input_location>/<location_bias>")
# def findPlaceFromUserText(input_location, location_bias):
#     API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={apiKey}&input={input_location}&inputtype={inputtype}&fields={fields}&locationbias={locationbias}"
#     inputtype = "textquery"
#     fields = "photos,formatted_address,name,rating,opening_hours,geometry,icon"
#     url_to_send = API_ENDPOINT.format(apiKey = API_KEY, input_location = input_location, inputtype = inputtype, fields = fields, locationbias = location_bias)
#     payload = {}
#     headers= {}
#     response = requests.request("GET", url_to_send, headers=headers, data = payload)
#     response = make_response(response.json())
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response

# @app.route("/getNearbyPlaces/<lat>/<lng>/<type>")
# def getNearbyPlaces(lat, lng, type):
#     API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={apiKey}&location={location}&radius={radius}&type={type}&language=en"
#     location = lat + "," + lng
#     radius = '50000' # in metres
#     url_to_send = API_ENDPOINT.format(apiKey = API_KEY, location = location, radius = radius, type = type)
#     payload = {}
#     headers= {}
#     response = requests.request("GET", url_to_send, headers=headers, data = payload)
#     response = make_response(response.json())
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response

# @app.route("/getPlacePhoto/<photo_reference>")
# def getPlacePhoto(photo_reference):
#     API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/photo?key={apiKey}&photoreference={photo_reference}&maxwidth={max_width}"
#     max_width = 450
#     # max_height = 250
#     url_to_send = API_ENDPOINT.format(apiKey = API_KEY, photo_reference = photo_reference, max_width = max_width)#, max_height = max_height)
#     payload = {}
#     headers= {}
#     response = requests.request("GET", url_to_send, headers=headers, data = payload)
#     response = make_response(response.url)
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response
    

if __name__=='__main__':
    app.run(port=5002, debug=True)
    app.run()
    