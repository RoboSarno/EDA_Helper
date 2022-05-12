import pandas as pd

def get_highcorr(df, col='', cor_val=0.5):
    '''
        Find high corr in a df for a specific col
    '''
    c = df.corr() # get correlation matrix
    s = c.unstack() # unpack correlation matrix
    so = s.sort_values(ascending=False, kind="quicksort") # sort correlation matrix
    corr_list_neg=[]
    corr_list_pos=[]
    for i, j in so.items():
        if (i[0] != i[1]) and (abs(j) >= cor_val): # check for 1 correlations
            if (j < 0):
                if ((i, j) not in corr_list_neg and (i[::-1], j) not in corr_list_neg) and (i[0] in [col] or i[1] in [col]):
                    corr_list_neg.append((i, j))
                
            else:
                if ((i, j) not in corr_list_pos and (i[::-1], j) not in corr_list_pos) and (i[0] in [col] or i[1] in [col]):
                        corr_list_pos.append((i,j))
            
        
    return corr_list_pos, corr_list_neg