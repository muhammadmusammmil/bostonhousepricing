import pickle
from flask import Flask, app, jsonify, request, url_for, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

#Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    print(output)
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)