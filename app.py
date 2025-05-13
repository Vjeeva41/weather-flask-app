from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "865e6d04c6077e4ba601cef04112540d"  # Get it from openweathermap.org

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": API_KEY, "units": "metric"}

            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    "city": city.title(),
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
                }
            else:
                error = "City not found 😓"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
