import pandas as pd
from oaf.data.processor import DataProcessor

def test_sales_summary():
    df = pd.DataFrame({
        "manager": ["AleX", "Alex", "Dzoni"],
        "amount": [100, 50, 200]
    })

    result = DataProcessor.sales_summary(df)

    assert result.loc[result.manager == "Alex", "total_sales"].iloc[0] == 150
    assert result.loc[result.manager == "Dzoni", "total_sales"].iloc[0] == 200
