import requests

base_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = "London,uk"  # город и код страны
api_key = "ddd7edd3fcb7f91dbac703663d22145f"  # ваш ключ API

params = {
    "q": city_name,
    "appid": api_key
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)