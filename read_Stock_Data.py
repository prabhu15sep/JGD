"""Reads the Stocks symbols and return Dataframe"""

import os
import pandas as pd

def list_to_path(list_name, base_dir="/Volumes/2/PyD/"):    #"C:\\Users\\ppadayac\\"
    """Return CSV file p  ath given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(list_name)))
    
def get_list(list_name,ind_key):
    df = pd.read_csv(list_to_path(list_name), index_col=ind_key,
    parse_dates=True, usecols=['Symbol', 'Series','ISIN Code'], na_values=['nan'])
    return df

def get_data(symbol,start_date,days):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    dates = pd.date_range(start=start_date, periods=20)
    df = pd.DataFrame(index=dates)
    
    df_temp = pd.read_csv(list_to_path(symbol), index_col='Date',
            parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

    df = df.join(df_temp)

    return df

    