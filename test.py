import eda_info as eda
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
# describe = eda.Describe(df)
# print(describe.col_info(['a']))

# issue = eda.Describe(df)
# numeric, numeric_issue, categorical, categorical_issue = issue.feature_issues()
# print(numeric, numeric_issue, categorical, categorical_issue)

corr = eda.Describe(df)
corr_list_pos, corr_list_neg = corr.get_highcorr('a', cor_val=0.5)
print(corr_list_pos, corr_list_neg)

# dist = eda.Distribution(df)
# dist.graph_distributions()






# print(ans.iloc[1, :]) # indexing the describe df


    
    
