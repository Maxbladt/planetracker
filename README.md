# planetracker
The reason for this project is to simplify the plane jet of Jack Sweeney. The code, written in Python, is under 400 lines long. Next to this it uses an easily available API so you can setup a similar project in no time. The aim for this project was to familiarize myself with calling API's, JSON, iterating over writing and sorting CSV files, working with a virtual machine and working in Google cloud.Next steps in the project to add a picture with the custom flight path of the plane. To add a function in which users can text to this twitter account and request a log of this plane.

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


