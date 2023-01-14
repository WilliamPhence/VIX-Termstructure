# Import libraries
import matplotlib.pyplot as plt
import pandas as pd

# Declare variables for the files we will be using, provide exact object link 
vix_9D_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX9D_History_2019.csv"
vix_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX_History_2019.csv"
vix_3M_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX3M_History_2019.csv"
vix_6M_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX6M_History_2019.csv"
vix_1Y_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX1Y_History_2019.csv"

def read_vx_data():
    # Open the files & create pandas dataframes
    df_9D = pd.read_csv(vix_9D_file)
    df_vx = pd.read_csv(vix_file)
    df_3M = pd.read_csv(vix_3M_file)
    df_6M = pd.read_csv(vix_6M_file)
    df_1Y = pd.read_csv(vix_1Y_file)

    # Reduce data frames to be only dates & closing marks for each index
    df_9D = df_9D[['9d_CLOSE', 'DATE']]
    df_vx = df_vx[['vx_CLOSE','DATE']]
    df_3m = df_3M[['3m_CLOSE', 'DATE']]
    df_6m = df_6M[['6m_CLOSE', 'DATE']]
    df_1Y = df_1Y[['1Y_CLOSE','DATE']]

    # Create a dataframe and add a new column for each index
    df_merged = pd.merge(df_9D, df_vx, on=['DATE'])
    df_merged = pd.merge(df_merged, df_3m, on=['DATE'])
    df_merged = pd.merge(df_merged, df_6m, on=['DATE'])
    df_merged = pd.merge(df_merged, df_1Y, on=['DATE'])

    # Calculate Ratios and add to merged dataframe
    df_merged['VX1Y/VX'] = df_merged['1Y_CLOSE'] / df_merged['vx_CLOSE']
    df_merged['VX1Y/VX9D'] = df_merged['1Y_CLOSE'] / df_merged['9d_CLOSE']
    df_merged['VX1Y/VX3M'] = df_merged['1Y_CLOSE'] / df_merged['3m_CLOSE']
    df_merged['VX1Y/VX6M'] = df_merged['1Y_CLOSE'] / df_merged['6m_CLOSE']
    df_merged ['DATE'] = pd.to_datetime(df_merged['DATE'], utc = True)

    # Move date column to be first one
    headers = list(df_merged.columns)
    headers[0],headers[1] = headers[1],headers[0]
    df_merged = df_merged[headers]

    # Create a csv file of the final merged dataframe to store and use
    df_merged.to_csv('vx_data.csv')

    return df_merged