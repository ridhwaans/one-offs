#!/usr/bin/env python

"""This program tests zero path, happy path, and negative paths in compare_forecasts_test.py at the unit level and integration level.
"""

__author__ = 'Ridhwaan Shakeel'
__date__ = 'August 04, 2016'
__email__ = 'shakeel.ridhwaan@gmail.com'
__version__ = '1.0.0'

import compare_forecasts
import unittest
import responses

class compare_forecasts_test(unittest.TestCase):

    API_KEY = "fe9c5cddb7e01d747b4611c3fc9eaf2c"

    def setUp(self):        
        compare_forecasts.main.forecast_hour = 4
        
    def test_01(self):
        """Check if the program validates a null city name before requesting the weather forecast
        """
        with self.assertRaises(ValueError) as test1:
                compare_forecasts.validate(None)
        self.assertEqual(
            'City name may not be empty',
            str(test1.exception)
        )

    def test_02(self):
        """Check if the program validates an empty city name before requesting the weather forecast
        """
        with self.assertRaises(ValueError) as test2:
                compare_forecasts.validate('')
        self.assertEqual(
            'City name may not be empty',
            str(test2.exception)
        )

    def test_03(self):
        """Check if the program validates a bad (non-existent/ special characters) city name before requesting the weather forecast
        """
        with self.assertRaises(ValueError) as test3:
                compare_forecasts.validate('unknowncityfoobar&&@')
        self.assertEqual(
            'City name may not be invalid',
            str(test3.exception)
        )

    def test_04(self):
        """Test if the program returns a 5 day weather forecast json response given a valid city request
        """
        city_forecast = compare_forecasts.get_forecast("Toronto")
        self.assertEquals(city_forecast.has_key('weather_description'), True)
        self.assertEquals(city_forecast.has_key('temperature'), True)
        # check that the 5 day forecast response has a set of five weather descriptions and temperatures
        self.assertEquals(len(city_forecast['weather_description']), 5)
        self.assertEquals(len(city_forecast['temperature']), 5)

    def test_05(self):
        """Test if the program successfully outputs a 5 day forecast comparison between two cities given Toronto and Cleveland
        """
        raised = False
        try:
            compare_forecasts.compare_forecasts('Toronto', 'Cleveland')
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    def test_06(self):
        """Test if the program gives a forecast comparison if the API request is for an unknown city
        """
        with self.assertRaises(ValueError) as test6:
            city_forecast = compare_forecasts.get_forecast("unknownCity")
        self.assertEqual(
            'City requested does not match',
            str(test6.exception)
        )
        
    @responses.activate  
    def test_07(self):
        """Test if the program works when the weather forecast service is unavailable
        """
        # mock the weather forecast service to be down
        responses.add(**{
          'method'         : responses.GET,
          'url'            : 'http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}'.format('Toronto', compare_forecasts_test.API_KEY),
          'body'           : '{"error": "504 Gateway timeout could not get a response from the server"}',
          'status'         : 504,
          'content_type'   : 'application/json',
          'adding_headers' : {'X-Foo': 'Bar'}
        })
        with self.assertRaises(RuntimeError) as test7:
            city_forecast = compare_forecasts.get_forecast("Toronto")
        self.assertEqual(
            'Weather forecast API service unavailable',
            str(test7.exception)
            )

if __name__ == "__main__":
    unittest.main()
