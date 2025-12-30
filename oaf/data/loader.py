import pandas as pd

class DataLoader:
    @staticmethod
    def csv(path: str) -> pd.DataFrame:
        return pd.read_csv(path)

    @staticmethod
    def excel(path: str) -> pd.DataFrame:
        return pd.read_excel(path)
