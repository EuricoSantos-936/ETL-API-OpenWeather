# Weather Data ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline that extracts weather data from the Open-Meteo API, transforms it into a structured format, and loads it into a SQLite database. Additionally, it saves the data as a CSV file.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [License](#license)

## Project Overview

The pipeline performs the following steps:
1. **Extract**: Retrieves weather data from the Open-Meteo API based on user-provided city coordinates.
2. **Transform**: Converts the raw API response into a structured DataFrame with relevant weather metrics.
3. **Load**: Saves the transformed data into an SQLite database and a CSV file.

## Technologies Used

- **Python**: Programming language used for writing the ETL pipeline.
- **Pandas**: Data manipulation library for transforming data.
- **SQLAlchemy**: SQL toolkit for loading data into an SQLite database.
- **Requests**: Library for making HTTP requests to the Open-Meteo API.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/euricosantos-936/ETL-Pipeline-OpenMeteoApi.git
   cd weather-etl-pipeline
    ```
2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ``` 

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```
## How to Run

1. **Run the Script**

    Execute the script using Python:
    
    ```bash
    python app.py
    ```

    Follow the Prompts

    When prompted, enter the name of the city for which you want to retrieve weather data.

## Usage

The script performs the following actions:

    . Requests weather data for the specified city using the Open-Meteo API.
    . Transforms the data into a Pandas DataFrame.
    . Saves the DataFrame to a CSV file named weather_data_<city>.csv.
    . Loads the data into an SQLite database file named weather_<city>.db.

The <city> placeholder in filenames is replaced with the user-provided city name.
License

This project is licensed under the MIT License - see the LICENSE file for details.
