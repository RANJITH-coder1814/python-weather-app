import requests

API_KEY = "YOUR_API_KEY_HERE"   # Replace with your OpenWeather API Key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print(" City not found!")
        return

    print("\n Weather Report")
    print("-" * 30)
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']} %")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Condition: {data['weather'][0]['description'].title()}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
