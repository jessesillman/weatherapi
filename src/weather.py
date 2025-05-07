from dotenv import load_dotenv
import os
import requests

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))  # Lataa .env projektin juuresta

API_KEY = os.getenv("OWM_API_KEY")
CITY = "Helsinki"

def get_weather():
    if not API_KEY:
        raise ValueError("API-avain puuttuu! Tarkista .env-tiedosto.")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    if 'main' not in data or 'temp' not in data['main']:
        raise KeyError("API vastasi odottamattomassa muodossa")
    
    return data

if __name__ == "__main__":
    try:
        weather = get_weather()
        print(f"Sää Helsingissä: {weather['main']['temp']}°C")
    except Exception as e:
        print(f"Virhe: {str(e)}")