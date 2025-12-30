import pandas as pd
from oaf.data.processor import process_dataframe

def test_process_dataframe_adds_total():
    df = pd.DataFrame({
        "A": [1, 2],
        "B": [3, 4]
    })

    result = process_dataframe(df)

    assert "TOTAL" in result.columns
    assert result["TOTAL"].tolist() == [4, 6]
