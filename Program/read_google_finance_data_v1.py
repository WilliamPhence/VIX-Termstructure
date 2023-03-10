# import libraries
import pandas as pd

def read_google_data(raw_data, start_date):

    # Open the files and create pandas data frames
    # Create one dataframe per variable & combine them later
    database = pd.read_csv(raw_data)

    spx = database[['Date', 'Close']].copy()
    vix_9D = database[['Date.1', 'Close.1']].copy()
    vix = database[['Date.2', 'Close.2']].copy()
    vix_3M = database[['Date.3', 'Close.3']].copy()
    vix_6M = database[['Date.4', 'Close.4']].copy()
    vix_1Y = database[['Date.5', 'Close.5']].copy()

    # Rename Column headers, start with Close columns
    spx.rename(columns= {'Close':'SPX_Close'}, inplace=True)
    vix_9D.rename(columns={'Close.1':'9D_Close'}, inplace=True)
    vix.rename(columns={'Close.2':'vx_Close'}, inplace=True)
    vix_3M.rename(columns={'Close.3':'3M_Close'}, inplace=True)
    vix_6M.rename(columns={'Close.4':'6M_Close'}, inplace=True)
    vix_1Y.rename(columns={'Close.5':'1Y_Close'}, inplace=True)

    # Rename Date column headers
    spx.rename(columns= {'Date':'Date'}, inplace=True)
    vix_9D.rename(columns={'Date.1':'Date'}, inplace=True)
    vix.rename(columns={'Date.2':'Date'}, inplace=True)
    vix_3M.rename(columns={'Date.3':'Date'}, inplace=True)
    vix_6M.rename(columns={'Date.4':'Date'}, inplace=True)
    vix_1Y.rename(columns={'Date.5':'Date'}, inplace=True)

    # Convert all datetime formats
    spx['Date'] = pd.to_datetime(spx['Date'], utc = True).dt.date
    vix_9D['Date'] = pd.to_datetime(vix_9D['Date'], utc = True).dt.date
    vix['Date'] = pd.to_datetime(vix['Date'], utc = True).dt.date
    vix_3M['Date'] = pd.to_datetime(vix_3M['Date'], utc = True).dt.date
    vix_6M['Date'] = pd.to_datetime(vix_6M['Date'], utc = True).dt.date
    vix_1Y['Date'] = pd.to_datetime(vix_1Y['Date'], utc = True).dt.date

    # Merge the Seperate Data frames
    df_merged = pd.merge(spx, vix_9D, on=['Date'])
    df_merged = pd.merge(df_merged, vix, on=['Date'])
    df_merged = pd.merge(df_merged, vix_3M, on=['Date'])
    df_merged = pd.merge(df_merged, vix_6M, on=['Date'])
    df_merged = pd.merge(df_merged, vix_1Y, on=['Date'])

    # cut off based on start date
    daatteee = df_merged['Date']
    print(f"merged data format : {type(daatteee)}")
    print(f"start date format : {type(start_date)}")
    start_date = pd.Timestamp(start_date)
    print(f"start date format post pandas: {type(start_date)}")
    ### THIS OUTPUTS SOME WARNING THAT IN FUTURE VERSIONS THIS COMPARISON WILL NOT WORK
    df_merged = df_merged.loc[df_merged['Date'] > start_date]

    # Calculate ratios and add to dataframe
    df_merged['VX1Y/VX'] = df_merged['1Y_Close'] / df_merged['vx_Close']
    df_merged['VX1Y/VX9D'] = df_merged['1Y_Close'] / df_merged['9D_Close']
    df_merged['VX1Y/VX3M'] = df_merged['1Y_Close'] / df_merged['3M_Close']
    df_merged['VX1Y/VX6M'] = df_merged['1Y_Close'] / df_merged['6M_Close']
    df_merged['VX3M/VX'] = df_merged['3M_Close'] / df_merged['vx_Close']

    # return final dataframe
    return df_merged