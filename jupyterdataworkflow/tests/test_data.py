import pandas as pd

from jupyterdataworkflow.data import get_Fremont_data

def test_Fremont_data():
    data = get_Fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
