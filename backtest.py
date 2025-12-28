import pandas as pd
import matplotlib.pyplot as plt

timeframe = "M15"
symbol = "SPX500"
timezone = "America/New_York"
start_range = "09:30"
end_range = "09:45"
latest_entry_time = "12:00"
min_ATR = 1.25
max_ATR = 3


def price_data(symbol):
    '''Load data for a given symbol from a CSV file and process it.

    Parameters
    ----------
    symbol : str
        The ticker symbol of the asset whose price data is being loaded.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the price data, with 'Datetime' as the index,
        localized to the specified timezone and filtered from '2020-12-31' onward.
    '''

    df = pd.read_csv(f"data/{symbol}_{timeframe}.csv",parse_dates=["Datetime"],index_col="Datetime")
    df.index = pd.to_datetime(df.index, utc=True).tz_convert(timezone)
    df = df.loc["2019-12-31":]
    return df

def real_opening_range(df):
    df['Time'] = df.index.time
    df['Date'] = df.index.date
   
