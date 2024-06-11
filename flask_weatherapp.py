import requests
from flask import Flask, redirect, request, render_template, flash
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b28d23ed689469a408245c16405bb049'

client = MongoClient('mongodb://localhost:27017/')
db = client['DB']
citeis = db['forms']

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
        oldcity = citeis.find_one({'city': city})
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        response = requests.get(url)
        if oldcity:
            flash('City already exists in the database.')
            return redirect('/')
        if city and response.status_code == 200:
            citeis.insert_one({'city': city}) 
        if response.status_code == 200:
            data = response.json()
            temperature_fahrenheit = data['main']['temp']
            temperature_celsius = (temperature_fahrenheit - 32) * 5/9
            weather_data = {
                'city': city,
                'temperature': round(temperature_celsius, 2),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
            return render_template('weather.html', weather_data=[weather_data])
        else:
            flash('City not found. Please try again.')
            return redirect('/')
    else:
        return render_template('weather.html', weather_data=[])

if __name__ == '__main__':
    app.run(debug=True)
