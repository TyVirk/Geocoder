## Geocoding by Tyler Virkler 10/3/2017

import requests
import csv
import json

count = 1
errors = 0
key = 'AIzaSyDDPu6B6ndB8LM9ikpnru5esSoRH9ZlMrg'

with open ('Geo4.csv', "wb") as f:
    writer = csv.writer(f)
    with open('All.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                print count
                bno = row[0]
                street = row[1]
                city = row[2]
                state = row[3]
              
              
                response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + bno + street + ',' + city +',' + state + '&key=' + key)


                data = response.json()
                lat = data
                print lat
                writer.writerow([lat])
                
                count += 1
                    

              