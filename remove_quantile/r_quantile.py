from matplotlib.pyplot import axes
import pandas as pd
import numpy as np
from scipy import stats

def remove_outliers(df, ignore_col = [], low=0.20, high=0.80):
    '''
        Removes outlier that are 5% from the left end data and 5% of the right end data
    '''

    cols = df.select_dtypes('number').columns  # limits to a (float), b (int) and e (timedelta)
    cols = [i for i in cols if i not in ignore_col]
    df_sub = df.loc[:, cols]
    # quantile filter: discard 1% upper / lower values
    lim = np.logical_or(df_sub < df_sub.quantile(high, numeric_only=False),
                        df_sub > df_sub.quantile(low, numeric_only=False))
    df.loc[:, cols] = df_sub.where(lim, np.nan)
    df = df.dropna(how='any', subset=cols)
    return df

# df = df[~((df[col] < (feature_value_less_than_3sigma)) |(df[col] > (feature_value_greater_than_3sigma)))]

# df = df.query('~(%s < @feature_value_less_than_3sigma or %s > @feature_value_greater_than_3sigma)' %(col, col))