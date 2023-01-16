# Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_SPX_vs_ratios(data_file, start_date, end_date):

    # Create a dataframe using the data from the csv file
    df_data = pd.read_csv(data_file)

    # format Date to be in datetime & set index equal to dates
    df_data['Date'] = pd.to_datetime(df_data['Date'], utc=True).dt.date
    df_data.set_index('Date', inplace=True)

    # Create a plot & Declare first axis
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Create lines for VIX Ratios
    line_spx, = ax1.plot( 
        df_data['SPX_Close'], 
        label='SPX'
    )
    line_1y_ratio, = ax2.plot( 
        df_data['VX1Y/VX'], 
        label='VX1Y/VIX', c='red'
    )
    line_3M_ratio, = ax2.plot( 
        df_data['VX3M/VX'], 
        label='VX3M/VIX', c='green'
    )

    # Plot lines & format figure
    # Format and create legend
    fig.legend(
        (line_spx, 
         line_1y_ratio,
         line_3M_ratio
         ), 
        ('SPX',
         'VIX1Y/VIX',
         'VIX3M/VIX',
         ),
        loc='lower right')    

    # Format the axes
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b-%y'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax1.set_title(f'SPX vs VIX TS Ratios({start_date}) to ({end_date})')
    ax1.set_ylabel("SPX Closing Marks")
    ax2.set_ylabel('Ratio(s) Closing Marks')
    ax1.set_xlabel('Dates (Month-Year)')
    plt.savefig(f"C:\Python Projects\VIX Term Structure Project\\figures\ SPX vs Ratios {start_date} to {end_date}.png", dpi=1000, bbox_inches='tight', pad_inches=0.5)
    plt.show()