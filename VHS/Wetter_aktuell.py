from pyowm import OWM
API_key = "4f8d872d0b9788fbde2666ef5e25f13e"

owm=OWM(API_key)

print(owm.get_API_key())

while True:

    obs = owm.weather_at_place('Munich,DE')

    w: object = obs.get_weather()

    print(w.get_clouds())
    print(w.get_rain())
    print(w.get_snow())
    print(w.get_wind())
    print(w.get_humidity())
    print(w.get_pressure())

    print(obs.get_reception_time(timeformat='iso'))
    time.sleep(60)

