from random import random

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define an empty dictionary to store weather data
weather_data = {}

# Error handling for Bad Request (400)
# @app.errorhandler(400)
# def bad_request_error(error):
#     return jsonify({'error': 'Bad request'}), 400
#
# # Error handling for Not Found (404)
# @app.errorhandler(404)
# def not_found_error(error):
#     return jsonify({'error': 'Not found'}), 404
#
# # Error handling for Internal Server Error (500)
# @app.errorhandler(500)
# def internal_server_error(error):
#     return jsonify({'error': 'Internal server error'}), 500

# Welcome message and documentation for the API
@app.route('/')
def index():
    return """Welcome to the Weather API!
    Endpoints:
    - GET /weather?location=<location>: Get weather data for a specific location.
    - POST /weather: Add new weather data for a location.
    - PUT /weather/<location>: Update weather data for a location.
    - DELETE /weather/<location>: Delete weather data for a location.
    """

# Route for getting weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    """Get weather data for a specific location."""
    location = request.args.get('location')

    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400

    # Make a request to your weather API to get real weather data
    response = requests.get('YOUR_WEATHER_API_ENDPOINT', params={'location': location})

    # Check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()  # Extract the weather data from the response
        return jsonify(weather_data), 200  # Return the weather data as JSON
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code  # Return an error message if the request failed


# Route for adding weather data
@app.route('/weather', methods=['POST'])
def add_weather():
    """Add new weather data for a location."""
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'location' not in data:
        return jsonify({'error': 'Location parameter is required'}), 400
    if 'temperature' not in data or not isinstance(data['temperature'], (int, float)):
        return jsonify({'error': 'Temperature must be a number'}), 400
    if 'dewPoint' not in data or not isinstance(data['dewPoint'], (int, float)):
        return jsonify({'error': 'Dew Point must be a number'}), 400
    if 'humidity' not in data or not isinstance(data['humidity'], (int, float)) or not (0 <= data['humidity'] <= 100):
        return jsonify({'error': 'Humidity must be a number between 0 and 100'}), 400
    if 'windSpeed' not in data or not isinstance(data['windSpeed'], (int, float)):
        return jsonify({'error': 'Wind Speed must be a number'}), 400
    if 'sunsetTime' not in data:
        return jsonify({'error': 'Sunset Time parameter is required'}), 400
    if 'moonPhase' not in data:
        return jsonify({'error': 'Moon Phase parameter is required'}), 400

    location = data['location']
    temperature = data['temperature']
    dewPoint = data['dewPoint']
    humidity = data['humidity']
    windSpeed = data['windSpeed']
    sunsetTime = data['sunsetTime']
    moonPhase = data['moonPhase']

    weather_data[location] = {
        'temperature': temperature,
        'dewPoint': dewPoint,
        'humidity': humidity,
        'windSpeed': windSpeed,
        'sunsetTime': sunsetTime,
        'moonPhase': moonPhase
    }

    return jsonify({'message': 'Weather data added successfully'}), 201

# Route for updating weather data
@app.route('/weather/<location>', methods=['PUT'])
def update_weather(location):
    """Update weather data for a location."""
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'temperature' not in data or not isinstance(data['temperature'], (int, float)):
        return jsonify({'error': 'Temperature must be a number'}), 400
    if 'dewPoint' not in data or not isinstance(data['dewPoint'], (int, float)):
        return jsonify({'error': 'Dew Point must be a number'}), 400
    if 'humidity' not in data or not isinstance(data['humidity'], (int, float)) or not (0 <= data['humidity'] <= 100):
        return jsonify({'error': 'Humidity must be a number between 0 and 100'}), 400
    if 'windSpeed' not in data or not isinstance(data['windSpeed'], (int, float)):
        return jsonify({'error': 'Wind Speed must be a number'}), 400
    if 'sunsetTime' not in data:
        return jsonify({'error': 'Sunset Time parameter is required'}), 400
    if 'moonPhase' not in data:
        return jsonify({'error': 'Moon Phase parameter is required'}), 400

    if location not in weather_data:
        return jsonify({'error': f'Weather data for {location} not found'}), 404

    weather_data[location]['temperature'] = data['temperature']
    weather_data[location]['dewPoint'] = data['dewPoint']
    weather_data[location]['humidity'] = data['humidity']
    weather_data[location]['windSpeed'] = data['windSpeed']
    weather_data[location]['sunsetTime'] = data['sunsetTime']
    weather_data[location]['moonPhase'] = data['moonPhase']

    return jsonify({'message': f'Weather data for {location} updated successfully'}), 200

# Route for deleting weather data
@app.route('/weather/<location>', methods=['DELETE'])
def delete_weather(location):
    """Delete weather data for a location."""
    if location not in weather_data:
        return jsonify({'error': f'Weather data for {location} not found'}), 404

    del weather_data[location]

    return jsonify({'message': f'Weather data for {location} deleted successfully'}), 204

def generate_simulated_weather(location):
    """Generate simulated weather data."""
    # Example of generating simulated weather data
    simulated_data = {
        'location': location,
        'temperature': round(random.uniform(-20, 40), 2),  # Temperature in Celsius
        'dewPoint': round(random.uniform(-20, 40), 2),     # Dew Point in Celsius
        'humidity': round(random.uniform(0, 100), 2),      # Humidity in percentage
        'windSpeed': round(random.uniform(0, 30), 2),      # Wind Speed in km/h
        'sunsetTime': '18:30',                             # Sunset Time (example format)
        'moonPhase': 'Waning Gibbous'                      # Moon Phase (example)
    }
    return simulated_data

if __name__ == '__main__':
    app.run(debug=True)
