import pandas as pd

class DataLoader:
    @staticmethod
    def from_excel(path: str):
        return pd.read_excel(path)
