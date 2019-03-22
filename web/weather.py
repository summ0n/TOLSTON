import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        "key": "ff1b9ce7dde4426d9a5200655191903",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
              return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
        return False
    return weather

if __name__ == "__main__":
    w = weather_by_city("Moscow,Russia")
    print(w)



