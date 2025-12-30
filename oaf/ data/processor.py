def process_dataframe(df):
    df["TOTAL"] = df.select_dtypes("number").sum(axis=1)
    return df
