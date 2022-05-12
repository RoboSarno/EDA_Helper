import get_feature_issue as gfi
import remove_quantile as rq
import get_high_corr as ghc
import eda_info as bd
import pandas as pd
import numpy as np


# df = pd.read_csv('./data/citibike_feb2014.csv')

    
df = pd.DataFrame({'a': list(np.random.rand(8)) + [123456, np.nan],       # float64
                   'b': [0,1,2,3,np.nan,5,6,np.nan,8,9],                  # int64
                   'c': [np.nan] + list("qwertzuio"),                     # object
                   'd': [pd.to_datetime(_) for _ in range(10)],           # datetime64[ns]
                   'e': [pd.Timedelta(_) for _ in range(10)],             # timedelta[ns]
                   'f': [True] * 5 + [False] * 5,                         # bool
                   'g': pd.Series(list("abcbabbcaa"), dtype="category")}) # category

# print(df)

# # testing better_describe
describe = bd.Describe(df)
print(describe.col_info(['a', 'k']))

# print(ans.iloc[1, :]) # indexing the describe df


# # testing get_transform_list
# num, num_issue, cat, cat_issue = gfi.get_transform_list(df)
# print(num, num_issue, cat, cat_issue)

# testing remove_outliers
# df = rq.remove_outliers(df, ignore_col=['e'])
# print(df)

    
    
