pathu = {
    "coord": {"lon": 76.2167, "lat": 10.5167},
    "weather": [
        {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}
    ],
    "base": "stations",
    "main": {
        "temp": 305.14,
        "feels_like": 309.04,
        "temp_min": 305.14,
        "temp_max": 305.14,
        "pressure": 1008,
        "humidity": 56,
        "sea_level": 1008,
        "grnd_level": 1007,
    },
    "visibility": 10000,
    "wind": {"speed": 3.88, "deg": 296, "gust": 5.62},
    "clouds": {"all": 85},
    "dt": 1664184193,
    "sys": {
        "type": 1,
        "id": 9211,
        "country": "IN",
        "sunrise": 1664153043,
        "sunset": 1664196547,
    },
    "timezone": 19800,
    "id": 1254187,
    "name": "Thrissur",
    "cod": 200,
}

weather = pathu['weather'][0]['description']
print(weather)

wind = pathu['wind']['deg']
print(wind)

sys = pathu['sys']['country']
print(sys)

main = pathu['main']['humidity']
print(main)
weather = pathu['weather'][0]['main']
print(weather)

wind = pathu['wind']['speed']
print(wind)
