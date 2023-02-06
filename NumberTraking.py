import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

import os

Key = input("Enter geocoder API Number: ")

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print("Victem number location is : ",yourLocation)

#get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print("Victem number service provider is : ",carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print("Victem number location",lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

##save map in html file
if os.path.exists("mylocation.html"):
  os.remove("mylocation.html")

myMap.save("myLocation.html")

