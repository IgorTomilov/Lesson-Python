from pyowm import OWM

owm = OWM('747e0b601ab68259ae79fec77ba09f68')  # You MUST provide a valid API key

mycity = input('Enter your city :')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(mycity)
w = observation.weather
temperature = w.temperature('celsius')

print(f'In {mycity} average temperature : {temperature["temp"]}')
print(f'Wind: {w.wind()}, humidyty: {w.humidity}')


w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}


observation_list = mgr.weather_around_coords(-22.57, -43.12)