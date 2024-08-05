#importing libraries
from flask import Flask, render_template, request 
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('occupancy.pkl', 'rb'))

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route('/prediction', methods=['POST', 'GET']) 
def predict():
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Light = float(request.form['Light'])
    CO2 = float(request.form['CO2'])
    HumidityRatio = float(request.form["HumidityRatio"])
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    
    total = [[Temperature, Humidity, Light, CO2, HumidityRatio, year, month, day]]
    y_test=model.predict(total)
    print(y_test)
    
    if(y_test==[0]):
        ans="It is not Occupied"
    else:
        ans="It is Occupied"
        return render_template("index.html", showcase = ans)

if __name__=="__main__":
    app.run(debug=False)