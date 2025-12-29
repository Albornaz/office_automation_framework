import pandas as pd

class DataProcessor:
    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        """Удаляет все строки с пропущенными значениями."""
        return df.dropna()

    @staticmethod
    def pivot(df: pd.DataFrame, index: str, columns: str, values: str) -> pd.DataFrame:
        """Создает сводную таблицу с суммированием значений."""
        return df.pivot_table(
            index=index,
            columns=columns,
            values=values,
            aggfunc="sum"
        )

    @staticmethod
    def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
        """Группирует по менеджеру (регистронезависимо) и суммирует amount."""
        df_copy = df.copy()
        df_copy['manager_lower'] = df_copy['manager'].str.lower()
        result = df_copy.groupby('manager_lower', as_index=False)['amount'].sum()
        result = result.rename(columns={'amount': 'total_sales'})
        original_names = df_copy.drop_duplicates('manager_lower')[['manager_lower', 'manager']]
        result = result.merge(original_names, on='manager_lower', how='left')
        return result[['manager', 'total_sales']]



