def null_ct(df, col):
    temp=df[col].isnull().sum()/len(df[col])*100
    return(temp.round(2))