from weather_client import get_weather, add_weather, update_weather, delete_weather

if __name__ == '__main__':
    print(get_weather('Delhi'))
    print(add_weather('Mumbai', 30, 25, 60, 15, '19:00', 'Waxing Gibbous'))
    print(update_weather('Mumbai', 32, 27, 65, 17, '19:30', 'Full Moon'))
    print(delete_weather('Mumbai'))
