import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
weatherTemp = json_data['main']['temp']
weatherHumidity = json_data['main']['humidity']
weatherVisibility = json_data['visibility']
print('Temp: ', weatherTemp, '\n', 'Humidity: ', weatherHumidity, '\n', 'Visibility: ', weatherVisibility)
