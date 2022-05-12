def get_transform_list(df, ingnore_col=[]):
    '''
        function to get the columns of categorical, columns of missing categorical, columns of numeric, columns of missing numeric, and columns that are continous and unique in value
    '''
    
    numeric = [col for col in df.select_dtypes(include=['number']) if col not in ingnore_col]
    numeric_issue = [col for col in numeric if df[col].isna().sum() != 0]
    numeric = [col for col in numeric if col not in numeric_issue]


    categorical = [col for col in df.select_dtypes(exclude=['number']) if col not in ingnore_col]
    categorical_issue = [col for col in categorical if df[col].isna().sum() != 0]
    categorical = [col for col in categorical if col not in categorical_issue]
    
    # print(len(numeric_issue) + len(numeric) + len(categorical_issue) + len(categorical) + len(high_card))
    return numeric, numeric_issue, categorical, categorical_issue