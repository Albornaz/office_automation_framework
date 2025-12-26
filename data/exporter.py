class DataExporter:
    @staticmethod
    def to_excel(df, path: str):
        df.to_excel(path, index=False)
