"""
Load and merge census data
"""

def merge_census(census_data, census_map, print_debug = False):
    """
    Combines the census data and map to one dataframe.

    The data is merged based on the GeoUID, renamed id. Unnecessary columns are dropped.

    :param census_data: pandas dataframe from census data csv
    :param census_map: pandas dataframe from census map geojson
    :param print_debug: print debug statements. Default is False.
    :return: pandas dataframe
    """
    # Copy
    census_data = census_data.copy()
    census_map = census_map.copy()

    if print_debug:
        print("initial census data")
        print(census_data.head())
        print(census_map.head())

    # Set index to GeoUID
    census_data.set_index("GeoUID", inplace=True)
    census_data.index.name = "id"

    census_map.set_index("id", inplace=True)
    # Change index type
    census_map.index = census_map.index.astype(int)

    if print_debug:
        print("prepared census data")
        print(census_data.head())
        print(census_map.head())

    census = census_map.merge(census_data, on="id")

    if print_debug:
        print("merged census data")
        print(census.head())

    # Now lets get rid of all the fluff
    print('Census files merged.')
    return census.drop(["name", "ruid", "rpid", "rgid", "rguid", "q", "Region Name"], axis=1)


