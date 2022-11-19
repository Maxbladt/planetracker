# Planetracker 
The reason for this project is to simplify the plane jet of Jack Sweeney. The code, written in Python, is under 400 lines long. Next to this it uses an easily available API so you can setup a similar project in no time. The aim for this project was to familiarize myself with calling API's, JSON, iterating over writing and sorting CSV files, working with a virtual machine and working in Google cloud.Next steps in the project to add a picture with the custom flight path of the plane. To add a function in which users can text to this twitter account and request a log of this plane.

# How the program works

This plane bot uses the RAPID API of ADSB to send a tweet out whenever a plane with a certain callsign takes off or lands. Initial purpose whas to track the King and government of the Netherlands across their flights. Next to this it shows the flight and distance of the plane when it has landed.Every time the bot is run it creates two files: A log file and a CSV file. The aim of the log file is to log every event in the program and show any exceptions or errors which can be used for debugging. The plane CSV file stores where the plane has landed, at what time and what the time was the plane took to go from one place to another and the distance. From the CSV handlers the only thing you need is the:<[small_medium_big_airports.csv(https://github.com/Maxbladt/planetracker/blob/main/CSV_handlers/small_medium_big_airports.csv)>. The rest of the programs are used to change from all airports to the airports of interest.To start this bot on your own the only two things you need are a Twitter development account and the rapid API of ADSB ($10.00 per month).

If you happen to have some improvements then please contribute to this project.
## Example takeoff Tweet
![Screenshot of Tweet landing](./images/takeoff.png)

## Example landing Tweet
![Screenshot of Tweet landing](./images/landing.png)


## Usage
Please follow these steps to get your application up and running:

1. Buy RAPID API. This is about $10.00 a month for about 10.000 requests; https://rapidapi.com/adsbx/api/adsbexchange-com1/. Fill in these API keys in Class.py

2. Get twitter developer and get your API keys. Fill in these API keys under the correct variables and run some tests. Do this before Elon Musk shuts all bots down.

3. Fill in the correct CALLSIGN and ICAO code. The Call sign and corresponding ICAO code can easily be found by going to http://flightradar24.com.

4. I used Google cloud - Ubuntu environment to host this script. It is very lightweight and you get $300.00 free credit in the first couple months.

5. To let the script run in the background on google cloud I use the following command: nohup python3 -u Main.py &>> activity.log& . This will start the program and run it till either the condition is False or till it is stopped by an external factor.

6. To stop the script the following technique I found to work best. This kills the Nohup branch: pstree -p ├─python3(2233)───{python3}(2312) kill -9 2233
 
### Requirements
The following packages are required for this script to work.
- python version 3 or higher
- pandas
- requests
- geopy

To install these packages, you can simply run: `pip install package`


