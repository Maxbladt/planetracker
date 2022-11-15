import time
from .Class import *
from Tweet_generator import create_tweet, ISO_country_to_continent
import logging
from flight_log_writer import flight_log, get_latest_flight_time, get_latest_flight_distance, get_latest_flight_costs

#Update this one. First number is small number next to big number. second number is ICAO 6 number digit. instance of PHGGOV is: plane("PHGOV", "485920")
CALLSIGN = "PHGOV"
HEXCODE = "485920"

Plane_instance = plane(CALLSIGN, HEXCODE)


#variables
plane_states = ["on_ground", "flying"]

plane_actions = ["opstijgen", "landen"]

#logging the file to see exceptions and problems and how the program handels these

logging.basicConfig(level=logging.INFO, 
format = "{asctime} {levelname:<8} {message}",
style="{",
filename= f'{CALLSIGN}_jet.log',
filemode = 'a'
)

# Time per cycle (seconds, minutes). default is 6 minutes per cycle. change them so they are both equal. this is important.

Original_time_per_cycle = convert_minutes_to_seconds(0,8)
Time_cycle = convert_minutes_to_seconds(0, 8)
Time_high_alert_cycle = convert_minutes_to_seconds(30, 0)

def Time_sleep_changer(new_time):
    
    global Time_cycle

    Time_cycle = new_time

#Keeps program running:
plane_on = True

#Ensures there is a clear divider when program is terminated and rerun aggain
logging.info(f"\n\n---------------------------------NEW LOG STARTED---------------------------------\n\n")

# main script:
def main():
    
    while plane_on == True:
        
        logging.info(f"Waiting {Time_cycle} seconds to do another api call.")
        
        time.sleep(Time_cycle)
        try:
            
            response = Plane_instance.get_response_if_on()['total']
            logging.info(f"Response transponder collected succesfully: {response}")
            status_plane = Plane_instance.get_status()
            logging.info(f"Plane_instance.get_status() collected succesfully: {status_plane}")
            
        except Exception as e:
            logging.critical("Exception occured: ", exc_info=True)
            continue

    
        
        #Check if plane is still on ground
        if response == 0 and status_plane == plane_states[0]:
            logging.info(f"Plane's transponder is off so plane is still on the ground")
            continue
            
        

        # Check when transponder comes on from plane that is on the ground if it already departed
        elif response == 1 and status_plane == plane_states[0]:

            
            try:
                ground_speed = Plane_instance.get_ground_speed()
                logging.info(f"Ground speed collected succesfully {ground_speed}")
            except Exception as e:
                logging.critical("Exception occured: ", exc_info=True)
                continue
            

            if ground_speed > 130:
               
                Plane_instance.change_status(plane_states[1])
                logging.info(f"Changed plane states to: {Plane_instance.get_status()}")
                Time_sleep_changer(Original_time_per_cycle)
                logging.info(f"Time has been changed to original time per cycle: {Time_cycle}")
                

                try:
                    nearest_airport = Plane_instance.get_nrst_airport()
                    log = flight_log(nearest_airport[1][0], CALLSIGN, "opstijgen",nearest_airport[1][3], nearest_airport[1][4])
                    logging.info(f"Plane log has been updated. succesfully using the following data. Airport: {nearest_airport[1][0]} Callsign: {CALLSIGN} Lon coordinates: {nearest_airport[1][3]} Lat coordinates: {nearest_airport[1][4]}")
                    logging.info(f"Coordinates of plane are: {Plane_instance.get_lat()},{Plane_instance.get_lon()}")
                    logging.info(f"Nearest airport found: {nearest_airport}")
                    post_result = create_tweet(CALLSIGN, nearest_airport[1][0], ISO_country_to_continent(nearest_airport[1][2], nearest_airport[1][0]), plane_actions[0], nearest_airport[1][3], nearest_airport[1][4])
                    logging.warning(f"Tweet placed with following info:  {post_result}")
                
                except Exception as e:
                    logging.critical("Exception occured: ", exc_info=True)
                    continue


            elif ground_speed < 130:
                logging.info(f"Plane's transponder is on but still on ground")
                Time_sleep_changer(Time_high_alert_cycle)
                logging.warning(f"Plane's transponder is on but still on ground. Time has been changed to high alert cycle.")
            
            else:
                logging.warning(f"Speed does not satisy any of the conditionals")



            
        
        # Check if plane is still flying
        elif response == 1 and status_plane == plane_states[1]:
            logging.info(f"Plane response is {response}  and status plane is {status_plane}, Plane is considred still flying.")
        
        # When the plane is flying check if it already landed or is still flying.
        elif response == 0 and status_plane == plane_states[1]:
            Plane_instance.change_status(plane_states[0])
            logging.info(f"Changed plane states to: {Plane_instance.get_status}")
            Time_sleep_changer(Original_time_per_cycle)
            logging.info(f"Time has been changed to original time per cycle: {Time_cycle}")

            try:
                nearest_airport = Plane_instance.get_nrst_airport()
                log = flight_log(nearest_airport[1][0], CALLSIGN, "landen",nearest_airport[1][3], nearest_airport[1][4])
                logging.info(f"Plane log has been updated. succesfully using the following data. Airport: {nearest_airport[1][0]} Callsign: {CALLSIGN} Lon coordinates: {nearest_airport[1][3]} Lat coordinates: {nearest_airport[1][4]}")
                logging.info(f"Coordinates of plane are: {Plane_instance.get_lat()},{Plane_instance.get_lon()}")
                logging.info(f"Nearest airport found: {nearest_airport}")
                post_result = create_tweet(CALLSIGN, nearest_airport[1][0], ISO_country_to_continent(nearest_airport[1][2], nearest_airport[1][0]), plane_actions[1], nearest_airport[1][3], nearest_airport[1][4], get_latest_flight_time(CALLSIGN), get_latest_flight_distance(CALLSIGN), get_latest_flight_costs(CALLSIGN))
                logging.warning(f"Tweet placed with following info:  {post_result}")



            
            except Exception as e:
                logging.critical("Exception occured: ", exc_info=True)
                continue
        
        else:
            logging.warning(f"Response does not satisy any of the conditionals")


        
        

#class operator to start program        
if __name__ == "__main__":
    main()

    









        
