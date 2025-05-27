# TODO Fix this mess
import numpy as np

def z_score(self):
    """
    Normalize all columns of a dataframe.
    :return: pandas dataframe with Z score
    """
    return (self - self.mean()) / self.std()
    
def remove_outliers(self, threshold):
    return self[np.abs(self < threshold).all(axis=1)]

def percentiles(self):
    max = self.max()
    return (self / max) * 100