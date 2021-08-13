from django.shortcuts import render
import requests,json
# Create your views here.
def home(request):
   
    city=request.POST.get('fname')
    url="http://api.weatherstack.com/current?access_key=19d13d1aa9e1395ecdff87e58d5dd984&query={}"
    rr=requests.get(url.format(city)).json()
    r=requests.get(url.format("Dhaka")).json()
    print(rr)
    try:
        city_weather={

            'tempkey':rr['current']['temperature'],
            'feelslikekey':rr['current']['feelslike'],
            'timekey':rr['location']['localtime'],
            'windspeeddkey':rr['current']['wind_speed'],
            'iconkey':rr['current']['weather_icons'][0],
            'citykey':rr['location']['name'],
            }
    except Exception:
        city_weather={
            'tempkey':r['current']['temperature'],
            'feelslikekey':r['current']['feelslike'],
            'timekey':r['location']['localtime'],
            'windspeeddkey':r['current']['wind_speed'],
            'iconkey':r['current']['weather_icons'][0],
            'citykey':r['location']['name'],
        }
    return render(request,'weatherapp/index.html',{'cityweatherkey':city_weather})  