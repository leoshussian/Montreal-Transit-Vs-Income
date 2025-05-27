import geopandas as gpd
import fastparquet
import pyarrow

from Transit_Quality_Study.transit_quality_study.config import stop_data_path

# Map stops to census areas
def get_stop_location(gtfs, census):
    # Drop unnecessary columns
    print('Creating stop_location')
    stop_location = (
        gtfs.stops
        .drop(columns=['stop_id', 'stop_name', 'stop_url', 'wheelchair_boarding', 'parent_station'])
    )
    # Spatially join stop_location and census
    stop_location = gpd.sjoin(stop_location, census, how='left', predicate='within')
    # Remove duplicate stations and set index
    stop_location = (stop_location
                     .drop_duplicates(['stop_code'])
                     .set_index('stop_code')
                     )
    return stop_location

def get_stop_routes(gtfs):
    # Map routes to stops
    # Drop stop_times repeated stop + route combinations
    print('Creating stop_routes')
    stop_routes = (
        gtfs.stop_times
        .drop_duplicates(['stop_code', 'route_id'])
        .groupby(['stop_code', 'stop_name', 'stop_url'])
        .agg(list)
    )
    # Drop the fluff
    stop_routes.drop(
        ['arrival_time', 'trip_id', 'service_id', 'direction_id', 'shape_id',
         'wheelchair_boarding', 'stop_id', 'stop_sequence', 'departure_time',
         'geometry', 'stop_lat', 'stop_lon', 'location_type','parent_station'],
        axis=1,
        inplace=True)
    return stop_routes

def get_stop_data(gtfs, census, allow_parquet = True):
    if stop_data_path.exists() and allow_parquet:
        return gpd.read_parquet(stop_data_path)
    else:
        print("Creating stop_data")
        stop_routes = get_stop_routes(gtfs)
        stop_location = get_stop_location(gtfs, census)
        # Combine stop_routes and stop_location
        stop_data = stop_routes.merge(stop_location, how='left', on=['stop_code'])

        # We drop more unused columns
        stop_data = (stop_data
                     .drop(columns = ['Type', 't', 'hh', 'dw', 'a', 'pop', 'index_right'])
                     .rename(columns = {'v_CA21_6: Population density per square kilometre':'Density',
                                        'v_CA21_906: Median total income of household in 2020 ($)': 'Income'}))
        # Make it a GeoDataFrame
        stop_data = gpd.GeoDataFrame(stop_data, geometry=stop_data.geometry)
        # Let's add stop names!
        stop_data = stop_data.sjoin(gtfs.stop_freq[['geometry', 'stop_name']]
                            .drop_duplicates('geometry'))
        temp = stop_data.pop('stop_name')
        stop_data.insert(0, 'stop_name', temp)
        # And we ship it off!
        stop_data.to_parquet(stop_data_path)
        print("stop_data saved as parquet to", stop_data_path)
        return stop_data