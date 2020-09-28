# WeatherData
A short script in Python that adds current weather data from the free OpenWeatherMap API to any shapefile. The skeleton of the program can be changed to retrieve data from any API you wish, but for this script I chose weather data as a sort of proof of concept.

# Motivation

In my work in Geographic Information Systems, oftentimes I cannot find datasets that fulfill every requirement for my projects. I might have found a shapefile that contains the exact geometry I'm looking for, but is missing a few attributes I need for analysis. There is a wealth of APIs on the web that provide a variety of data, many of them for free. Instead of endlessly scrounging the web for the perfect dataset, I wrote this script to pull data from an API and customize my existing shapefiles with new attributes, saving lots of time in the process. 

# Dependencies
1. Runs on any Python 3.x interpreter.
2. Works only with shapefiles.
3. Requires gdal and ogr packages (https://gdal.org/download.html).

# Program Overview/Directions
1. Run the weather_data.py in your interpreter of choice
2. It will prompt you for the path of your Shapefile. Copy/paste the file path. 
3. The program will create three attributes in your shapefile and populate values from OpenWeatherAPI 

# Notes
1. The program adds the data directly to your shapefile, meaning the change is permanent unless you directly remove the added data. It may help to create a copy of your shapefile before running the program. 
2. Repeated requests may not work, as I only have a free license with OpenWeather. 

#Known Issues
1. There seems to be a problem with my API key. You may have to sign up with OpenWeather and receive your own key. 
