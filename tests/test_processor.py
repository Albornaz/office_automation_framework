import pandas as pd
from oaf.data.processor import DataProcessor

# ------------------- TEST: sales_summary -------------------
def test_sales_summary():
    df = pd.DataFrame({
        "manager": ["AleX", "Alex", "Dzoni"],
        "amount": [100, 50, 200]
    })

    result = DataProcessor.sales_summary(df)

    assert result.loc[result.manager.str.lower() == "alex", "total_sales"].iloc[0] == 150
    assert result.loc[result.manager.str.lower() == "dzoni", "total_sales"].iloc[0] == 200

# ------------------- TEST: clean -------------------
def test_clean():
    df = pd.DataFrame({
        "A": [1, 2, None],
        "B": [None, 2, 3]
    })

    cleaned = DataProcessor.clean(df)

    assert cleaned.isnull().sum().sum() == 0
    assert len(cleaned) == 1  # только вторая строка не имеет NaN

# ------------------- TEST: pivot -------------------
def test_pivot():
    df = pd.DataFrame({
        "Category": ["Fruit", "Fruit", "Vegetable", "Vegetable"],
        "Type": ["Apple", "Banana", "Carrot", "Broccoli"],
        "Amount": [10, 20, 15, 5]
    })

    pivoted = DataProcessor.pivot(df, index="Category", columns="Type", values="Amount")

    assert pivoted.loc["Fruit", "Apple"] == 10
    assert pivoted.loc["Fruit", "Banana"] == 20
    assert pivoted.loc["Vegetable", "Carrot"] == 15
    assert pivoted.loc["Vegetable", "Broccoli"] == 5

