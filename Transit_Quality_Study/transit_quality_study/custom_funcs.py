# TODO Fix this mess
import numpy as np

def z_score(df):
    """
    Normalize all columns of a dataframe.
    :param df: DataFrame
    :return: Z-score normalized DataFrame
    """
    return (df - df.mean()) / df.std()
    
def remove_outliers(self, threshold):
    return self[np.abs(self < threshold).all(axis=1)]

def percentiles(self):
    max = self.max()
    return (self / max) * 100