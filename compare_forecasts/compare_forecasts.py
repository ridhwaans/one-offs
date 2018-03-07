#!/usr/bin/env python

"""This script takes in two city names as input and outputs the differences in
weather between the cities over the next 5 days.

Usage example:

    python compare_forecasts.py Toronto Cleveland

Output example:

    Weather forecast comparison between Toronto and Cleveland:

    Day 1:
    Toronto (18C) will be 3C cooler than Cleveland (21C).
    Toronto will have clear sky, but Cleveland will have rain.

    Day 2:
    Toronto (21C) will be 3C warmer than Cleveland (18C).
    Toronto will have scattered clouds, but Cleveland will have light rain.

    Day 3:
    Toronto and Cleveland will both have the same temperature (20C).
    Toronto and Cleveland will both have light rain.

    Day 4:
    Toronto (18C) will be 3C cooler than Cleveland (21C).
    Toronto and Cleveland will both have light rain.

    Day 5:
    Toronto and Cleveland will both have the same temperature (17C).
    Toronto will have scattered clouds, but Cleveland will have light rain.
"""

__author__ = 'Ridhwaan Shakeel'
__date__ = 'August 04, 2016'
__email__ = 'shakeel.ridhwaan@gmail.com'
__version__ = '1.0.0'

import argparse
import requests

EPOCH_DAY = 86400
EPOCH_HOUR = 3600
TEMPERATURE = "temperature"
WEATHER_DESCRIPTION = "weather_description"
API_KEY = "fe9c5cddb7e01d747b4611c3fc9eaf2c"

def main():
    """Main method that takes in two city names and a forecast time as input.
    Calls compare_forecasts to get and make a weather forecast comparison.
    """
    parser = argparse.ArgumentParser(description="Compare weather forecasts between two cities.")
    parser.add_argument("city1", type=str, help="The first city.")
    parser.add_argument("city2", type=str, help="The second city.")
    args = parser.parse_args()
    while True:
        time = raw_input ("Choose a forecast time (UTC) for the 5 day forecast (ENTER to continue):\n 1) 00:00, 2) 03:00, 3) 06:00, 4) 09:00, 5) 12:00, 6) 15:00, 7) 18:00, 8) 21:00 :")
        # check if the forecast hour is specified in the list
        if time in ['1', '2', '3', '4', '5', '6', '7', '8']:
            main.forecast_hour = int(time)
            break
    compare_forecasts(args.city1, args.city2)

def compare_forecasts(city1, city2):
    """Compares and displays the weather description and temperature forecasts between two cities for 5 days at a given forecast time.
    """
    print("Weather forecast comparison between {} and {}:".format(city1, city2))
    city1_forecast = get_forecast(city1)
    city2_forecast = get_forecast(city2)
    # iterate through the dictionaries of two cities to make a forecast comparison where the index is the day
    for index in range(len(city1_forecast['temperature'])):    
        print
        print("Day {}:".format(index+1))
        if (city1_forecast[TEMPERATURE][index]) == (city2_forecast[TEMPERATURE][index]):
            print("{} and {} will both have the same temperature ({}C).".format(city1, city2, city1_forecast[TEMPERATURE][index]))
        elif (city1_forecast[TEMPERATURE][index]) > (city2_forecast[TEMPERATURE][index]):
            print("{} ({}C) will be {}C warmer than {} ({}C).".format(city1, city1_forecast[TEMPERATURE][index], abs(city1_forecast[TEMPERATURE][index] - city2_forecast[TEMPERATURE][index]), city2, city2_forecast[TEMPERATURE][index]))
        elif (city1_forecast[TEMPERATURE][index]) < (city2_forecast[TEMPERATURE][index]):
            print("{} ({}C) will be {}C cooler than {} ({}C).".format(city1, city1_forecast[TEMPERATURE][index], abs(city1_forecast[TEMPERATURE][index] - city2_forecast[TEMPERATURE][index]), city2, city2_forecast[TEMPERATURE][index]))            
        if (city1_forecast[WEATHER_DESCRIPTION][index]) == (city2_forecast[WEATHER_DESCRIPTION][index]):
            print("{} and {} will both have {}.".format(city1, city2, city1_forecast[WEATHER_DESCRIPTION][index]))
        else:
            print("{} will have {}, but {} will have {}.".format(city1, city1_forecast[WEATHER_DESCRIPTION][index], city2, city2_forecast[WEATHER_DESCRIPTION][index]))        

def get_forecast(city):
    """Uses the http://openweathermap.org/forecast5 API to get a forecast JSON response for one city.
    Builds a dictionary to hold weather description and temperature forecast for 5 days
    """
    validate(city)
    try:
        city_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}'.format(city, API_KEY))
        city_request.raise_for_status()  
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        raise RuntimeError('Weather forecast API service unavailable') # ping check if the server times out i.e. HTTP 504
    except requests.exceptions.HTTPError: # catch other HTTP status errors
        raise RuntimeError('An error has occurred while trying to make a request to the weather forecast API service')
    else:
        if (city.lower() != city_request.json()['city']['name'].lower()):
            raise ValueError('City requested does not match')
    # the JSON response has eight sets of weather forecast data per day (one set every 3 hours);
    # query the unixtimes (JSON key 'dt') in the JSON response to select one set of forecast data each day at the chosen hour
    expr = (item for item in city_request.json()['list'] if (item['dt'] % EPOCH_DAY / EPOCH_HOUR) == (main.forecast_hour-1)*3)
    # get a list of the city's weather descriptions and temperatures at a given forecast time every day for 5 days
    city_forecast = {}
    for x in expr:
        city_forecast.setdefault(TEMPERATURE, []).append(int(x['main']['temp'] - 273.15))
        city_forecast.setdefault(WEATHER_DESCRIPTION, []).append(x['weather'][0]['description'])
    return city_forecast

def validate(city):
    """Validates the city name string.
    """
    if (city == None or city.strip() == ""):
        raise ValueError('City name may not be empty')
    elif not all(x.isalpha() or x.isspace() for x in city):
        raise ValueError('City name may not be invalid')        
    
if __name__ == "__main__":
    main()
