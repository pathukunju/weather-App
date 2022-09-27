from flask import Flask, render_template,request
import requests

app = Flask("weather")

@app.route('/',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('spot')
        
        print(data)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid=0c1f63f761e0caf78712ec7b00736ec0'
        print(url)
        api_data = requests.get(url)
        python_dict = api_data.json()
        print(python_dict)
        pathu = python_dict['weather'][0]['description']

        print(pathu)
        wind = python_dict['wind']['speed']
        print(wind)
        pressure = python_dict['main']['pressure']
        humidity = python_dict['main']['humidity']
        temperature = python_dict['main']['temp']
        sys = python_dict['sys']['country']
        
    
        return render_template('index.html',data=data, pathu =pathu, wind =wind,humidity=humidity,temperature = temperature,sys =sys,pressure =pressure)

    else:


        return render_template('index.html')


app.run()