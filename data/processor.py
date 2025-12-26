class DataProcessor:
    @staticmethod
    def clean(df):
        return df.dropna()

    @staticmethod
    def pivot(df, index, columns, values):
        return df.pivot_table(
            index=index,
            columns=columns,
            values=values,
            aggfunc="sum"
        )
