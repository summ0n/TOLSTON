from flask import Flask
from weather import weather_by_city


app = Flask(__name__)

@app.route('/')
def func01():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return f"Температура: По Цельсию(C): {weather['temp_C']}C, По Фаренгейту(F): {weather['temp_F']}F, ощущается как {weather['FeelsLikeC']}C"
    else:
        return 'Прогноз погоды не доступен!'
if __name__ == '__main__':
    app.run(debug=True)

