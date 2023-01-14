# Import useful libraries
import matplotlib.pyplot as plt
import pandas as pd

# Declare variables for the files we will be using, provide exact object link 
vx_data_file = 'C:\Python Priojects\VIX Term Structure Project/vx_data.csv'
spx_file = "C:\Python Priojects\VIX Term Structure Project\Data\SPX_HistoricalPrices_2019.csv"

def read_spx_data():
    # Read the spx file contents into a dataframe with only date and closing marks. Convert time to standard format
    df_spx = pd.read_csv(spx_file)
    df_spx['DATE'] = pd.to_datetime(df_spx['DATE'], utc = True)
    df_spx = df_spx[['DATE', 'spx_CLOSE']]

    # reverse the order of the dataframe so that it is from oldest to newest dates
    df_spx = df_spx[::-1]

    # read the vix data file we made from 'read_vx_data.py' into a dataframe
    df_vix = pd.read_csv(vx_data_file)
    df_vix['DATE'] = pd.to_datetime(df_vix['DATE'], utc=True)

    # merge the spx and vix data frames into one
    df_final = pd.merge(df_spx, df_vix, on=['DATE'])

    # Delete the column of index values carried from df_vix
    del df_final['Unnamed: 0']

    # Create and save final dataframe to a csv
    df_final.to_csv('SPX_VIX_Ratios_data.csv')
    
    return df_final