from pathlib import Path
__all__ = ['data_dir', 'gtfs_feed_path', 'census_data_path', 'census_map_path', 'gtfs_data_dir', 'stop_data_path']

project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "data"

gtfs_feed_path = "https://www.stm.info/sites/default/files/gtfs/gtfs_stm.zip"

census_data_path = data_dir / "raw" / "Montreal_census_data.csv"
census_map_path = data_dir / "raw" / "Montreal_census_map.geojson"
gtfs_data_dir = data_dir / "raw" / "gtfs_data"

processed_data_dir = data_dir / 'processed'
stop_data_path = processed_data_dir / 'stop_data.parquet'

EPSG = 2950 # CRS in Montreal