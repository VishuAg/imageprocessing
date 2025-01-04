# from geopy.geocoders import Nominatim
from googletrans import Translator
import asyncio
# from googletrans import AsyncTranslator
# Initialize the geolocator and translator
# geolocator = Nominatim(user_agent="myExercises")

# Function to get location from latitude and longitude
# def get_location_from_coordinates(lat, lon):
#     location = geolocator.reverse((lat, lon), language='en')
#     return location.address if location else "Location not found."

import requests

def get_location_from_lat_lon(lat, lon):
    api_key= "AIzaSyDyTUMeZdWWXaI6N_INlIdvUVlXPXkN-zc" 
    # Google Maps Geocoding API endpoint
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}"
    
    # Send a GET request to the Google API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            # Extract the formatted address
            location = data['results'][1]['formatted_address']
            return location
        else:
            return "Location not found"
    else:
        return f"Error: {response.status_code}"


# Function to translate the address to Hindi
async def getLocationName(latitude, longitude):
    location_in_english = get_location_from_lat_lon(latitude, longitude)
    print(location_in_english)
    return await transliterate_to_hindi(location_in_english)

# # Input Latitude and Longitude
# latitude = float(input("Enter latitude: "))
# longitude = float(input("Enter longitude: "))

# Get the location in English
async def transliterate_to_hindi(text):
    # Initialize the Translator
    translator = Translator()

    # Use the translate method and await it
    translated = await asyncio.to_thread(translator.translate, text, 'en', 'hi')

    # Return the translated text
    return translated.text

# Translate the location to Hindi
# location_in_hindi = getLocationName(latitude, longitude)

# Output the result
# print(f"Location in Hindi: {location_in_hindi}")

# import requests

# def get_location_from_coordinates(lat, lon):
#     url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&addressdetails=1"
#     response = requests.get(url, verify=False)  # Bypass SSL verification
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return "Error: Unable to fetch data"

# latitude = 67.87
# longitude = 45.76
# location = get_location_from_coordinates(latitude, longitude)
# print(location)