# Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt

# Declare variable(s) for the files we will be using, provide exact object link 
data_file = 'C:\Python Priojects\VIX Term Structure Project/SPX_VIX_Ratios_data.csv'

# Create a dataframe using the data from the csv file
df_data = pd.read_csv(data_file)

headers = df_data.columns
for header in headers:
    print(header)

# Create a plot & Declare first axis
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

# Create lines for VIX Ratios
line_spx = ax1.plot(df_data['DATE'][-100:], df_data['spx_CLOSE'][-100:], label='SPX')
line_1y_ratio = ax2.plot(df_data['DATE'][-100:], df_data['VX1Y/VX'][-100:], label='VX1Y/VIX', c='red')

# Create a list of lines we are plotting
lines = line_spx + line_1y_ratio
labels = [l.get_label() for l in lines]

# Plot lines & format figure
ax1.legend(lines, labels)
plt.xticks([])
plt.show()