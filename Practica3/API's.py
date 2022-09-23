import requests
for i in range (5):
    city = input('Introduzca la ciudad que desea consultar: ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=00569ee2cb156b64aeca9feb8bfd0b00&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    lat = data["coord"]["lat"]
    longitude = data["coord"]["lon"]
    description = data["weather"][0]["description"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]

    print('********************Consulta ',i+1,'********************')
    print('Temperatura: ', temp)
    print('Velocidad del viento:', wind_speed)
    print('Latitud: ', lat)
    print('Longitud: ', longitude)
    print('Descripcion: ', description)
    print('Temperatura Max: ', temp_max)
    print('Temperatura Min: ',temp_min)
    if description == 'overcast clouds':
        nubes = data["clouds"]["all"]
        print('Nivel de nubes: ', nubes,"%")
    print('*******************************************************************************************************')

