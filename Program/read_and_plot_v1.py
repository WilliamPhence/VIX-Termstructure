# Import custom functions
from plot_SPX_vs_Ratios import plot_SPX_vs_ratios
from plot_SPX_vs_Vol_Indexes import plot_SPX_vs_vol_indexes
from read_google_finance_data_v1 import read_google_data
from delete_temp_files import delete_temp_files

import pandas as pd
from datetime import date

# Declare variables for the files we will be using

# Raw data gets processed by read google data are for read_google_data
raw_data = 'C:\Python Projects\VIX Term Structure Project\data-master\DATA - MASTER.csv'

# This is the output of read google data that gets plotted by plot functions
data_file = 'C:\Python Projects\VIX Term Structure Project\data-master\MERGED DATA.csv'

# Declare folder path for temp files that will be deleted
temp_data = "C:\Python Projects\VIX Term Structure Project\\temp-data"

start_date = input("Provide a start date (YYYY-MM-DD) : ")
start_date_str = start_date
start_date = pd.to_datetime(start_date)
end_date = date.today()

# Run functions
read_google_data(raw_data, start_date)

# reformat start_date
start_date = start_date_str
plot_SPX_vs_ratios(data_file, start_date, end_date)
plot_SPX_vs_vol_indexes(data_file, start_date, end_date)

data = pd.DataFrame(pd.read_csv(data_file))

delete_temp_files(temp_data)