import os
import requests

from dotenv import load_dotenv


load_dotenv()


def get_weather(latitude, longitude):

    api_key = os.getenv(
        "OPENWEATHER_API_KEY"
    )

    if not api_key:

        return {
            "success": False,
            "message": "OpenWeather API key not configured."
        }

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        rainfall = data.get(
            "rain",
            {}
        ).get(
            "1h",
            0
        )

        return {
            "success": True,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": rainfall,
            "weather": data["weather"][0]["description"],
            "wind": data["wind"]["speed"]
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }