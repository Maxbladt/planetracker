# Import DictWriter class from CSV module
from csv import DictWriter, DictReader
import csv
import pandas as pd
from datetime import datetime

def time_difference(time_1, time_2):
    from datetime import datetime
    d1 = datetime.strptime(time_1, "%d/%m/%Y %H:%M")
    d2 = datetime.strptime(time_2, "%d/%m/%Y %H:%M")

    delta = d2 - d1
    return delta

def distance_from_coordinate( lat1, lon1, lat2, lon2):
    import geopy.distance
    coords_1 = (lat1,lon1 )
    coords_2 = (lat2, lon2)
    return geopy.distance.geodesic(coords_1, coords_2).km

def create_header(file, headerList):
    # open CSV file and assign header
    with open(file, 'w') as file:
        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
        dw.writeheader()
        file.close()





def get_latest_flight_distance(callsign):
    inputfile = f"{callsign}_flight_log.csv"
    with open(inputfile, "r") as flight_log:
        last_line = flight_log.readlines()[-1]
        # creates a list object that you can get the 6 objects from using their index
        last_line_log = last_line.split(",")

        return last_line_log[4]
        
def get_latest_flight_time(callsign):
    inputfile = f"{callsign}_flight_log.csv"
    with open(inputfile, "r") as flight_log:
        last_line = flight_log.readlines()[-1]
        # creates a list object that you can get the 6 objects from using their index
        last_line_log = last_line.split(",")

        return last_line_log[5]

def get_latest_flight_costs(callsign):
    inputfile = f"{callsign}_flight_log.csv"
    with open(inputfile, "r") as flight_log:
        last_line = flight_log.readlines()[-1]
        # creates a list object that you can get the 6 objects from using their index
        last_line_log = last_line.split(",")

        return last_line_log[6]
  
def see_if_CSV_created(callsign):
    try:

        with open(f"{callsign}_flight_log.csv", 'r') as log:
            reader_file = csv.reader(log)
            return 1
            
    except:
        return 0
    

def flight_log( airport, callsign, plane_action, lat_coordinates_approaching_airprt, lon_coordinates_approaching_airprt):


    inputfile = f"{callsign}_flight_log.csv"
    field_names = ["date", "airport", "callsign","plane_action", "distance", "flight_time", "costs_flight", "lat_coordinates", "lon_coordinates"]
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M")

    if see_if_CSV_created(callsign) == 0:
        create_header(inputfile, field_names)


    
    

    costs_flight = 0
    

    # Dictionary that we want to add as a new row

    if plane_action == "opstijgen":
        dict = {"date": date , "airport" : airport, "callsign" : callsign ,"plane_action": plane_action, "distance": "NA", "flight_time": "NA", "costs_flight":"NA", "lat_coordinates":lat_coordinates_approaching_airprt, "lon_coordinates": lon_coordinates_approaching_airprt }
    if plane_action == "landen":

        
        with open(inputfile, "r") as flight_log:
            last_line = flight_log.readlines()[-1]
            # creates a list object that you can get the 6 objects from using their index
            last_line_log = last_line.split(",")
    
            # Information from last flight used to calculate things like distance and costs of flight
            lat_coordinates = last_line_log[7]
            lon_coordinates = last_line_log[8]
            time_now = now.strftime("%d/%m/%Y %H:%M")
            #Variables that are calculated
            
            Time_of_flight = time_difference(last_line_log[0], time_now)
            distance_of_flight = round(distance_from_coordinate(lat_coordinates, lon_coordinates, lat_coordinates_approaching_airprt, lon_coordinates_approaching_airprt),2)
            costs_flight = round((distance_of_flight * 23.44), 2)
            dict = {"date": date , "airport" : airport, "callsign" : callsign ,"plane_action": plane_action, "distance": distance_of_flight, "flight_time": Time_of_flight, "costs_flight":costs_flight, "lat_coordinates":lat_coordinates_approaching_airprt, "lon_coordinates": lon_coordinates_approaching_airprt}
    
    


     
    else:
        dict = {"date": date , "airport" : airport, "callsign" : callsign ,"plane_action": plane_action, "distance": "NA", "flight_time": "NA", "costs_flight":"NA", "lat_coordinates":lat_coordinates_approaching_airprt, "lon_coordinates": lon_coordinates_approaching_airprt}



    with open(inputfile, 'a') as log:
        dictwriter_object = DictWriter(log, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        log.close()

schiphol = (52.308056, 4.764167)
lhw = (51.481147, -0.430723)
    

# flight_log("Schiphol", "EZY56AK", "opstijgen", schiphol[0], schiphol[1])

# flight_log("London Heathrow", "PHGOV", "landen", lhw[0], lhw[1])




