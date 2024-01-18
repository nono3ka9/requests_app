import requests

url = "https://weather.tsukumijima.net/api/forecast"

params = {
    "大阪": "270000",
    "兵庫": "280010",
    "奈良": "190010",
    "和歌山": "300010",
    "京都": "260010",
    "滋賀": "250010",
    "三重": "240010",
}

params2 = {
    "city":"270000"
}

response = requests.get(url)

print (response.json())