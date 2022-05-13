from xml.etree.ElementInclude import include
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

class Distribution:
    def __init__(self, df):
        self.df = df
        self.numeric_df = self.df.select_dtypes(include=['number', np.number])
        
    def remove_outliers(self, df, ignore_col = [], low=0.20, high=0.80):
        '''---------------------------------'''
        """_summary_

        Args:
            df (_type_): _description_
            ignore_col (list, optional): _description_. Defaults to [].
            low (float, optional): _description_. Defaults to 0.20.
            high (float, optional): _description_. Defaults to 0.80.

        Returns:
            _type_: _description_
        """
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
    
    def graph_distributions(self):
        '''---------------------------------'''
        """_summary_
        """
        for i in self.numeric_df.columns:
            plt.hist(x=self.numeric_df[i])
            plt.title(f'Distribution of {i}')
            plt.xlabel(f'{i}')
            plt.ylabel('Count')
            plt.show()

        