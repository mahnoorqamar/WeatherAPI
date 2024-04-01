import requests

BASE_URL = 'http://127.0.0.1:5000'  # Change this to match your Flask server address


def get_weather(location):
    url = f'{BASE_URL}/weather?location={location}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Print response content
    print(response.text)

    try:
        # Attempt to parse response as JSON
        return response.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return None


def add_weather(location, temperature, dew_point, humidity, wind_speed, sunset_time, moon_phase):
    url = f'{BASE_URL}/weather'
    data = {
        'location': location,
        'temperature': temperature,
        'dewPoint': dew_point,
        'humidity': humidity,
        'windSpeed': wind_speed,
        'sunsetTime': sunset_time,
        'moonPhase': moon_phase
    }
    response = requests.post(url, json=data)
    return response.json()

def update_weather(location, temperature, dew_point, humidity, wind_speed, sunset_time, moon_phase):
    url = f'{BASE_URL}/weather/{location}'
    data = {
        'temperature': temperature,
        'dewPoint': dew_point,
        'humidity': humidity,
        'windSpeed': wind_speed,
        'sunsetTime': sunset_time,
        'moonPhase': moon_phase
    }
    response = requests.put(url, json=data)
    return response.json()


def delete_weather(location):
    url = f'{BASE_URL}/weather/{location}'
    response = requests.delete(url)

    # Check if the request was successful
    if response.status_code != 204:
        print(f"Error: {response.status_code}")
        return None

    try:
        # Attempt to parse response as JSON
        return response.json()
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return None


if __name__ == '__main__':
    print(get_weather('New York'))
    print(add_weather('Los Angeles', 75, 65, 50, 10, '18:00', 'Waning Gibbous'))
    print(update_weather('Los Angeles', 80, 70, 55, 12, '18:30', 'Full Moon'))
    print(delete_weather('Los Angeles'))
