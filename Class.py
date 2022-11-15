import json
from collections import OrderedDict

import requests
import geopy.distance
import pandas as pd
import csv
Rapid_API_key = "Your_API_KEY"

#1. Functions to call api data


# Returns response if plane's transponder is on. total[1] == on. if on it shows a lot of data.
def get_response_if_on(callsign):
	headers_1 = {
	"X-RapidAPI-Key": Rapid_API_key,
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
}

	url = "https://adsbexchange-com1.p.rapidapi.com/v2/callsign/" + str(callsign) + "/"
	response_1 = requests.get( url, headers=headers_1).json()
	return response_1



# Returns if plane has flown in last 48 hours. first use get_response_callsign to see if plane is flying then this function.
def get_response_last_48_hours(hex_code):
	headers_2 = {
	"X-RapidAPI-Key": "79b3d94038msh1e55ced0085567ep1f8fafjsn65b137ace07f",
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"}
	url = "https://adsbexchange-com1.p.rapidapi.com/v2/hex/" + str(hex_code) + "/"
	
	response_2 = requests.get(url, headers=headers_2).json()
	return response_2
	

#2. General functions


def distance_from_coordinate( lat1, lon1, lat2, lon2):
		
		coords_1 = (lat1,lon1 )
		coords_2 = (lat2, lon2)
		
		return geopy.distance.geodesic(coords_1, coords_2).km

def convert_minutes_to_seconds(seconds=0, minutes=6):
	try:
		total_time = seconds + (minutes * 60)
		return total_time
	except:
		print("Wrong value input")
	
		
# 3. csv handler

#Max rows that are displayed. Can adjust for tests to see dataframe	
	

pd.options.display.max_rows = 999
data = pd.read_csv(r'small_medium_big_airports.csv')
df = pd.DataFrame(data, columns= ['id','type', 'name', 'latitude_deg', 'longitude_deg', 'elevation_ft', 'iso_country'])
	
#2 Class functions of plane



class plane(OrderedDict):
	def __init__(self, callsign, hexcode, flightstatus="on_ground"):
		self.callsign = str(callsign)
		self.hexcode = str(hexcode)
		self.flightstatus = str(flightstatus)
		
	
	def __str__(self):
		return str(self.get_response())


	def get_response_if_on(self):
		response = get_response_if_on(self.callsign)
		return response


	def get_response(self):
		response = get_response_last_48_hours(self.hexcode)
		return response
	
	
	def get_lat(self):
		return self.get_response()['lat']
	
	def get_lon(self):
		return self.get_response()['lon']
	
	def get_ground_speed(self):
		return self.get_response()['gs']
	
	def get_status(self):
	    return self.flightstatus
	
	def change_status(self, new_flightstatus):
		self.flightstatus = new_flightstatus
		return self.flightstatus

	
	def get_nrst_airport(self):
		dict = {}
		
		lat_1 = self.get_lat()
		lon_1 = self.get_lon()
		for index, row in df.iterrows():
			Distance = distance_from_coordinate(float(lat_1),float(lon_1), float(row['latitude_deg']), float(row['longitude_deg']))
			dict[Distance] = [row['name'], str(row['elevation_ft']), row['iso_country'], str(row['latitude_deg']), str(row['longitude_deg'])]
		
		sorted_dict = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))
		nearest_airport = next(iter(sorted_dict.items()))
		
		return nearest_airport





		
	

	








	


	

	

	



