import pandas as pd
import csv
from pathlib import Path

# Reads airports.csv and saves a zip file containing only small medium and large airports.

data = pd.read_csv(r'/Users/maxbladt/Desktop/Twitter_bot_V3/airports.csv')
Categories = ["small_airport", "medium_airport", "large_airport"]
only_airports = data[data.type.isin(Categories)]


compression_opts = dict(method='zip',
                        archive_name='small_medium_big_airports.csv')  
only_airports.to_csv('small_medium_big_airports.zip', index=False,
          compression=compression_opts)  










