import requests
import json
while True:
    print('Güncel hava durumu')
    city = str(input('Bir şehir girin: '))
    API_key = '6e3fed367662f65a17ddb269a2c4fac8'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=tr&appid={API_key}&units=metric')

    data = json.loads(response.text)

    if (data['cod']) == '404':
        print('Böyle bir şehir bulunamadı')

    else:
        print(f"{city} hava durumu")
        print(f"Sıcaklık: {data['main']['temp']} °C")
        print(f"Max sıcaklık: {data['main']['temp_max']}°C Min sıcaklık: {data['main']['temp_min']} °C")
        print(f"Hissedilen: {data['main']['feels_like']} °C")
        print(f"Basınç: {data['main']['pressure']} hPa")
        print(f"Nem: {data['main']['humidity']} %")
        print(f"Bulut: {data['weather'][0]['description']}")
        print(f"Rüzgar Hızı: {data['wind']['speed']} km/sa")
        break