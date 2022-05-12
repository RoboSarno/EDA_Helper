from locale import normalize
import pandas as pd
import numbers
import numpy as np
import datetime

class Describe:
    def __init__(self, df):
        self.df = df
        self.Bdescriber = self.better_describe()
        
    def consistent(self, u_values):
        """_summary_
            Helper function to check if all the unique values in a pandas column are a consitent data type.
        Args:
            u_values (list): unique values in a pandas df col

        Returns:
            bool: based on if all values in a df col are all the same or not
        """
        for val in range(len(u_values)):
            if  val == 0: # for first unique element
                first_dtype = type(u_values[val])
            else:
                if first_dtype != type(u_values[val]): # case when not consistent
                    return False
        return True
    
    def get_dtypes(self, u_values):
        """_summary_
            Helper function to get a data types

        Args:
            u_values (_type_): list of unique values in a pandas col

        Returns:
            set: of all data types in a pandas column
        """
        data_type_list = [type(u_values[val]) for val in range(len(u_values))]
        return set(data_type_list)

    def is_numeric(self, obj):
        """_summary_
            Helper function that checks if a object is a python numeric value
        Args:
            obj (dtype): object data type

        Returns:
            bool: True if an object is python numeric
        """
        attrs = ['__add__', '__sub__', '__mul__', '__truediv__', '__pow__']
        return all(hasattr(obj, attr) for attr in attrs)


    def col_better_describe(self, df, col):
        """_summary_
            Helper function to get eda describe info
        Args:
            df (pd.Dataframe): original pandas df to get info on
            col (col): col to get better describe info

        Returns:
            dict:  column name, continuous column, consistent data type, number of na values, data types in column, pd.value_counts, min, max , mean or mode depending on column type, standard deviation
        """
        shape = df.shape # shape of dataframe
        unique_values = list(df[col].unique()) # col unique values
        len_list = len(unique_values) # col len of unique values
        
        na_val = df[col].isna().sum() # get number of nana values
        is_consistent = self.consistent(unique_values) # check if unique values are consistent in datatype
        
        is_balanced = dict(round(100 * df[col].value_counts(normalize=True), 2))
        value_counts = dict(df[col].value_counts(dropna=False)) # values counts
        memory_usage = df[col].memory_usage(deep=True)

        dtime_dtypes = (
            datetime.date, datetime.time, datetime.datetime,
            datetime.timedelta, datetime.tzinfo, datetime.timezone
        )
        
        if is_consistent: # if not consistent
            d_type = type(df[col].iloc[0]) # if not consistent
        else:
            d_type = self.get_dtypes(unique_values) # if not consistent
            
        if isinstance(d_type, (numbers.Number)) or self.is_numeric(d_type): # if python numerical get min and max or if numpy numerical get min and max
            minimum = min(df[col])
            maximim = max(df[col])
            mean_mode = df[col].mean()
            std_dev = df[col].std() 
            
        elif isinstance(df[col].loc[0], dtime_dtypes): # if datetime numerical get min and max
            minimum = min(df[col])
            maximim = max(df[col])
            mean_mode = np.nan
            std_dev = np.nan

        
        else: # if categorical get min and max
            minimum = np.nan
            maximim = np.nan
            mean_mode = df.mode()[col][0]
            std_dev = np.nan
            
        # check if all values in a col are unique, get data type of col
        info = dict(col_name = col, continuous_col = (shape[0] == len_list), 
                    consistent_dtype = is_consistent, num_na=na_val, 
                    data_type = d_type, value_counts = value_counts, 
                    min = minimum, max = maximim, 
                    mean_mode = mean_mode, std=std_dev,
                    balance = is_balanced, mem_usage=memory_usage) 
        return info

    def better_describe(self):
        """_summary_
            Based on EDA process of cleaning a data. This function helps users describe information within a pandas dataset.
        Args:
            df (pd.dataframe): pandas dataframe uncleaned.

        Returns:
            pd.dataframe: Information about a specific data set to help with EDA.
        """
        ans = pd.DataFrame() # initialize dataframe
        col_info_list = [self.col_better_describe(self.df, col) for col in self.df.columns] # for each col in df
        ans = pd.DataFrame(col_info_list)
        ans.set_index('col_name', inplace=True)
        return ans
    
    def col_info(self, col_names):
        """_summary_

        Args:
            col_names (list(str)): List of column names you would like to see info about.

        Returns:
            pd.Dataframe: 
        """
        ans = pd.DataFrame()
        for col in col_names:
            temp = self.Bdescriber[self.Bdescriber.index.str.startswith(col)]
            if temp.empty:
                return f'Error :: Issue with col_names = {col_names}\n-------- Column name {col} does not exsist in DataFrame.'
            else:
                ans = pd.concat([ans, temp], axis=0)
        return ans
            
            
