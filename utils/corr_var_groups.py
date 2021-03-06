import numpy as np

def corr_var_groups(df,corr_tresh):
    """creates a list of lists with groups of variables that have a pearson correlation 
    bigger than corr_tresh among each other"""
    
    corrMatrix = df.corr()
    corrMatrix.loc[:,:] =  np.tril(corrMatrix, k=-1)

    already_in = set()
    result = []
    for col in corrMatrix:
        tresh_corr = corrMatrix[col][corrMatrix[col] >= corr_tresh].index.tolist()
        if tresh_corr and col not in already_in:
            already_in.update(set(tresh_corr))
            tresh_corr.append(col)
            result.append(tresh_corr)
    return result
