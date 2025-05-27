from pathlib import Path
__all__ = ['data_dir', 'gtfs_feed_path', 'census_data_path', 'census_map_path', 'gtfs_data_dir', 'stop_data_path']

data_dir = Path(r'C:\Users\Shawk\Documents\Concordia\Personal Projects\Transit Quality Study\data')

gtfs_feed_path = "https://www.stm.info/sites/default/files/gtfs/gtfs_stm.zip"

census_data_path = data_dir / r'raw\Montreal_census_data.csv'
census_map_path = data_dir / r'raw\Montreal_census_map.geojson'
gtfs_data_dir = data_dir / r'raw\gtfs_data'

processed_data_dir = data_dir / 'processed'
stop_data_path = processed_data_dir / 'stop_data.parquet'

EPSG = 2950 # CRS in Montreal