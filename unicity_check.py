def unicity_check(df, col):
    temp = df.duplicated(subset=col, keep=False)
    temp = temp.value_counts()
    return(temp)