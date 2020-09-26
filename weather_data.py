#Author: Dylan Coe

#Temperature Data for Shapefiles
#This program takes in a shapefile as input, and, creates fields in the
#shapefile for temperature (current, min, and max) and fills in the values using data from the OpenWeatherMap API


#import relevant packages
    #gdal/ogr- spatial data layer writing/management
    #requests- pull data from OpenWeatherMap API
    #os.path- work with file paths for the input
import gdal, ogr, requests, os.path

#Prompt user to enter Shapefile file name
shapefile_filename = input("Please enter the file path of your Shapefile (absolute or relative paths acceptable): ")
#Check if file exists, using os.path.isfile(filename), where "filename" is the path to the file that the user enters
while os.path.isfile(shapefile_filename) == False:
    shapefile_filename = input("\nThe file you have entered does not exist. Please try again: ")

#open shapefile
shapefile = ogr.Open(shapefile_filename)
drv = ogr.GetDriverByName("ESRI Shapefile")
file = drv.Open(shapefile_filename,1)
layer = file.GetLayer()

#create fields for current temperature, min temperature, max temperature in celcius
temp_field = ogr.FieldDefn('TEMP', ogr.OFTReal)
temp_field.SetWidth(5)
layer.CreateField(temp_field)

temp_min_field = ogr.FieldDefn('TEMP_MIN', ogr.OFTReal)
temp_min_field.SetWidth(5)
layer.CreateField(temp_min_field)

temp_max_field = ogr.FieldDefn('TEMP_MAX', ogr.OFTReal)
temp_max_field.SetWidth(5)
layer.CreateField(temp_max_field)

#iterate over each feature in the layer, finding centroid, retrieing data from api, creating fields, atnd attaching to shapefile
for feature in layer:
    #Get the geometry of the feature
    geom = feature.GetGeometryRef()
    #Find the point centroid of the feature
    centroid = geom.Centroid()
    #call NOAA API to retrieve temperature and precipitation data
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=6b4d66102c545def1b8961b0935fcfef' % (centroid.GetY(), centroid.GetX()))
    #convert to json
    r_json = r.json()

    #set variables for temp, convert from kelvin to farenheit

    temp_f = float(((r_json['main']['temp'])-273.15)*9/5+32)
    temp_min_f = float(((r_json['main']['temp_min'])-273.15)*9/5+32)
    temp_max_f = float(((r_json['main']['temp_max'])-273.15)*9/5+32)

    #set retrieved values to shapefile field
    feature.SetField('TEMP', temp_f)
    layer.SetFeature(feature)
    feature.SetField('TEMP_MIN', temp_min_f)
    layer.SetFeature(feature)
    feature.SetField('TEMP_MAX', temp_max_f)
    layer.SetFeature(feature)

file.Destroy()




