import requests

def get_elevation_from_open_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/elevation?latitude={lat}&longitude={lon}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        elevation = data['elevation']
        return elevation[0]
    else:
        print("Error fetching data")
        return None

# Example latitude and longitude
latitude = 20.1
longitude = 25.1

elevation = get_elevation_from_open_meteo(latitude, longitude)
if elevation is not None:
    print(f"Elevation: {elevation} meters")