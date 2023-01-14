# Import useful libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# Declare variables for the files we will be using, provide exact object link 
vix_9D_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX9D_History_2019.csv"
vix_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX_History_2019.csv"
vix_3M_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX3M_History_2019.csv"
vix_6M_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX6M_History_2019.csv"
vix_1Y_file = "C:\Python Priojects\VIX Term Structure Project\Data\VIX1Y_History_2019.csv"
spx_file = "C:\Python Priojects\VIX Term Structure Project\Data\SPX_HistoricalPrices_2019.csv"

# Open the files & print dataframes
df_9D =  pd.read_csv(vix_9D_file)
df_vx = pd.read_csv(vix_file)
df_3M = pd.read_csv(vix_3M_file)
df_6M = pd.read_csv(vix_6M_file)
df_1Y = pd.read_csv(vix_1Y_file)
df_spx = pd.read_csv(spx_file)

# Look for and get dates & closing marks for each index
df_9d_marks = df_9D[['9d_CLOSE', 'DATE']]
df_vx_marks = df_vx[['vx_CLOSE','DATE']]
df_3M_marks = df_3M[['3m_CLOSE', 'DATE']]
df_6M_marks = df_6M[['6m_CLOSE', 'DATE']]
df_1Y_marks = df_1Y[['1Y_CLOSE','DATE']]
df_spx_marks = df_spx[['spx_CLOSE', 'DATE']]

# Create a dataframe for the 1Y Ratio
df_9d_merged = pd.merge(df_9d_marks, df_vx_marks, on=['DATE'])
df_3m_merged = pd.merge(df_9d_merged, df_3M_marks, on=['DATE'])
df_6m_merged = pd.merge(df_3m_merged, df_6M_marks, on=['DATE'])
df_1y_merged = pd.merge(df_6m_merged, df_1Y_marks, on=['DATE'])


# Calculate Ratios and add to dataframe
df_1y_merged['VX1Y/VX'] = df_1y_merged['1Y_CLOSE'] / df_1y_merged['vx_CLOSE']
df_1y_merged['VX1Y/VX9D'] = df_1y_merged['1Y_CLOSE'] / df_1y_merged['9d_CLOSE']
df_1y_merged['VX1Y/VX3M'] = df_1y_merged['1Y_CLOSE'] / df_1y_merged['3m_CLOSE']
df_1y_merged['VX1Y/VX6M'] = df_1y_merged['1Y_CLOSE'] / df_1y_merged['6m_CLOSE']

df_1y_merged.to_csv('VIX Indicies Close and 1Y Ratios.csv')

# Create a plot & Declare first axis
fig, ax1 = plt.subplots()

# Create lines for VIX Ratios
#line_9dr = ax1.plot(df_1y_merged['DATE'], df_1y_merged['VX1Y/VX9D'], label='VX1Y/VX9D')
line_3mr = ax1.plot(df_1y_merged['DATE'][-100:], df_1y_merged['VX1Y/VX3M'][-100:], label='VX1Y/VX3M')
line_6mr = ax1.plot(df_1y_merged['DATE'][-100:], df_1y_merged['VX1Y/VX6M'][-100:], label='VX1Y/VX6M')
line_vxr = ax1.plot(df_1y_merged['DATE'][-100:], df_1y_merged['VX1Y/VX'][-100:], label='VX1Y/VIX')

# Plot SPX on second axis
ax1.legend()
plt.xticks([])
plt.show()