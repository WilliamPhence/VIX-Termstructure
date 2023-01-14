# Import custom functions
from plot_SPX_vs_Ratios import plot_SPX_vs_ratios
from plot_SPX_vs_Vol_Indexes import plot_SPX_vs_vol_indexes
from read_google_finance_data_v1 import read_google_data
import pandas as pd

# Declare variables for the files we will be using, provide exact object link 
# These are for read_google_data
data_file = 'C:\Python Projects\VIX Term Structure Project\Data\MERGED DATA.csv'
# This is for 1.1 versions
raw_data = 'C:\Python Projects\VIX Term Structure Project\Data\DATA - MASTER.csv'

# Run functions
read_google_data(raw_data)
plot_SPX_vs_ratios(data_file)
plot_SPX_vs_vol_indexes(data_file)

data = pd.DataFrame(pd.read_csv(data_file))

print(data)