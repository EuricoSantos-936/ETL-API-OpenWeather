import requests
import pandas as pd
from sqlalchemy import create_engine

# Get Coordinates Nominatim
def get_coordinates(city):
    geo_url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1'
    response = requests.get(geo_url)
    data = response.json()
    
    if response.status_code == 200 and len(data) > 0:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        print("Error accessing the Nominatim API or city not found.")
        return None, None

# Extract Weather Data
def extract_weather_data(lat, lon):
    url = (f'https://api.open-meteo.com/v1/forecast'
           f'?latitude={lat}'
           f'&longitude={lon}'
           f'&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
           f'&timezone=Europe/Lisbon')
    print("Requesting weather data from URL:", url)
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if response.status_code == 200:
        return data
    else:
        print("Error accessing the Open-Meteo API.")
        return None
    
# Transform Data
def transform_weather_data(data, lat, lon):
    if data:
        # Extract relevant data (modify this to fit the Open-Meteo data structure)
        hourly_data = data['hourly']
        df = pd.DataFrame({
            'timestamp': pd.to_datetime(hourly_data['time']),
            'temperature': hourly_data['temperature_2m'],
            'relative_humidity': hourly_data['relative_humidity_2m'],
            'wind_speed': hourly_data['wind_speed_10m'],
            'latitude': lat,
            'longitude': lon
        })
        return df
    else:
        return None


# Load Data into Database
def load_data_to_db(df, city, db_name='weather.db'):
    safe_city_name = city.replace(' ', '_').replace('/', '_').replace('\\', '_')
    db_name = f'weather_{safe_city_name}.db'
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql('weather', con=engine, if_exists='replace', index=False)
    print(f"Data loaded into SQLite database: {db_name}")

# Run the pipeline
city = input("Please enter the city name: ")
latitude, longitude = get_coordinates(city)

if latitude and longitude:
    weather_data = extract_weather_data(latitude, longitude)
    if weather_data:
        weather_df = transform_weather_data(weather_data,latitude, longitude)
        if weather_df is not None:
            csv_filename = f'weather_data_{city.replace(" ", "_").replace("/", "_").replace("\\", "_")}.csv'
            weather_df.to_csv(csv_filename, index=False)
            print(f"Data saved to {csv_filename}")
            load_data_to_db(weather_df, city)