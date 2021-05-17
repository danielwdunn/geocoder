import pandas as pd
import os
from geopy import geocoders
import csv
from geopy.geocoders import GoogleV3
from pandas import read_csv

apikey = "AAA"
g = GoogleV3(api_key=apikey)

#Input File
inputFile = 'GeocodeHamdenPropertyAssessment.csv'

#Output File
outputFile = 'hamdenLatitudeLongitude.csv'


#Read from CSV
data = read_csv(inputFile)
addresses = data['Concatenated Address'].tolist()


for a in addresses:
    try:
        inputAddress = a
        print(inputAddress)
        location = g.geocode(inputAddress, timeout=30)
        print(location.latitude, location.longitude)
        with open(outputFile, mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([location.latitude,location.longitude,a])
    except:
        print('Error, skipping address...')
        with open(outputFile, mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(['error','error',a])
