def forecast(*weather_data):
    sunny = []
    cloudy = []
    rainy = []
    result = ''
    for i in range(len(weather_data)):
        city, weather = weather_data[i][0], weather_data[i][1]

        if weather == 'Sunny':
            sunny.append(city)
        elif weather == 'Cloudy':
            cloudy.append(city)
        elif weather == 'Rainy':
            rainy.append(city)

    for city in sorted(sunny):
        result += f'{city} - Sunny\n'

    for city in sorted(cloudy):
        result += f'{city} - Cloudy\n'

    for city in sorted(rainy):
        result += f'{city} - Rainy\n'

    return result


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
