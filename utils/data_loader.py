import pandas as pd


def load_locations():

    return pd.read_csv(
        "data/locations.csv"
    )


def load_data(file_path):

    return pd.read_csv(file_path)