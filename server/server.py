from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/locations')
def all_locations():
    response = jsonify({'locations': util.locations()})
    response.headers.add('Access-Control-Allow-Origin', '*')

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = float(request.form['bath'])

    response = jsonify({'price': util.predict_price(location, total_sqft, bhk, bath)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()