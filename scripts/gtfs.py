from Transit_Quality_Study.transit_quality_study.config import gtfs_data_dir

import pandas as pd
import geopandas as gpd
import pyarrow
import fastparquet

class Gtfs:
    """
    Stores all the GTFS dataframes
    """

    def __init__(self, feed, use_parquet = True):
        """
        Generates the numerous GTFS dataframes offered by gtfs_functions.

        :param feed: gtfs_functions.Feed object
        """
        print('Processing GTFS files...')
        if self.has_parquet() and use_parquet:
            print('Parquet files found. Loading parquet files.')
            self.routes = pd.read_parquet(gtfs_data_dir / "routes.parquet")
            self.trips = pd.read_parquet(gtfs_data_dir / "trips.parquet")
            self.stops = gpd.read_parquet(gtfs_data_dir / "stops.parquet")
            self.stop_times = gpd.read_parquet(gtfs_data_dir / "stop_times.parquet")
            self.shapes = gpd.read_parquet(gtfs_data_dir / "shapes.parquet")
            self.stop_freq = gpd.read_parquet(gtfs_data_dir / "stop_freq.parquet")

        else: #TODO what
            self.routes = feed.routes.copy(deep = True)
            self.trips = feed.trips.copy(deep = True)
            self.stops = feed.stops.copy(deep = True)
            self.stop_times = feed.stop_times.copy(deep = True)
            self.shapes = feed.shapes.copy(deep = True)
            self.stop_freq = feed.stops_freq.copy(deep = True)
            # Processes GTFS files
            print('Successfully processed GTFS files.')
            self.to_parquet()

    def to_parquet(self):
        """
        Stores all GTFS dataframes in parquet format.
        """
        self.routes.to_parquet(path = gtfs_data_dir / "routes.parquet")
        self.trips.to_parquet(path = gtfs_data_dir / "trips.parquet")
        self.stops.to_parquet(path = gtfs_data_dir / "stops.parquet")
        self.stop_times.to_parquet(path = gtfs_data_dir / "stop_times.parquet")
        self.shapes.to_parquet(path = gtfs_data_dir / "shapes.parquet")
        self.stop_freq.to_parquet(path = gtfs_data_dir / "stop_freq.parquet")
        print("GTFS parquet files saved to", gtfs_data_dir)

    def has_parquet(self):
        """
        Checks if GTFS dataframes exist in parquet format.
        :return: boolean
        """
        return \
            ((gtfs_data_dir / "routes.parquet").exists()
            and (gtfs_data_dir / "trips.parquet").exists()
            and (gtfs_data_dir / "stops.parquet").exists()
            and (gtfs_data_dir / "stop_times.parquet").exists()
            and (gtfs_data_dir / "shapes.parquet").exists()
            and (gtfs_data_dir / "stop_freq.parquet").exists())