# Imports
import pandas as pd
import geopandas as gpd

# Local imports
from Transit_Quality_Study.transit_quality_study.config import *
from scripts import gtfs, census, stop_data
from gtfs_functions import Feed

# Initialize GTFS feed (no busiest_date, 24-hour time window)

print('Initializing GTFS feed...')
feed = Feed(gtfs_feed_path, busiest_date = False, time_windows=[0, 24])

gtfs = gtfs.Gtfs(feed)

print('Reading census files...')
census_data = pd.read_csv(census_data_path)
census_map = gpd.read_file(census_map_path)
print('Success.')
census = census.merge_census(census_data, census_map)

stop_data = stop_data.get_stop_data(gtfs, census)