from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request ,'request/index.html')

def detail(request):

    place = request.GET.get("place")
    print(place)

    response = requests.get("https://weather.tsukumijima.net/api/forecast/city/"+place)
    print(response.text)
    data = response.json()
    time = data["forecasts"][0]["date"]
    prefecture = data["location"]["prefecture"]
    img = data["forecasts"][0]["image"]["url"]
    weather = data["forecasts"][0]["detail"]["weather"]
    min = data["forecasts"][0]["temperature"]["min"]["celsius"]
    max = data["forecasts"][0]["temperature"]["max"]["celsius"]

    context = {
        "date":time,
        "prefecture":prefecture,
        "url":img,
        "weather":weather,
        "min":min,
        "max":max,
    }

    return render(request, 'request/detail.html', context)