# Import custom functions
from plot_SPX_vs_Ratios import plot_SPX_vs_ratios
from plot_SPX_vs_Vol_Indexes import plot_SPX_vs_vol_indexes
from read_google_finance_data_v1 import read_google_data

import pandas as pd
from datetime import date

# Raw data gets processed by read google data are for read_google_data
raw_data = 'C:\Python Projects\VIX Term Structure Project\data-master\DATA - MASTER.csv'

# Ask user for input & inform them about dataset limits
start_date = input("Provide a start date (2018-06-08 or later) : ")
# store the string input from the user
start_date_str = start_date
# format start date to datetime
start_date = pd.to_datetime(start_date)
end_date = date.today()

# This is the output of read google data that gets plotted by plot functions
data = read_google_data(raw_data, start_date)
data = pd.DataFrame(data)

# Run plot functions
plot_SPX_vs_ratios(data, start_date_str, end_date)
plot_SPX_vs_vol_indexes(data, start_date_str, end_date)