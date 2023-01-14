# Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt

def plot_SPX_vs_ratios(data_file):
# Create a dataframe using the data from the csv file
    df_data = pd.read_csv(data_file)

    # Create a plot & Declare first axis
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Create lines for VIX Ratios
    line_spx, = ax1.plot(
        df_data['Date'][:], 
        df_data['SPX_Close'][:], 
        label='SPX'
    )
    line_1y_ratio, = ax2.plot(
        df_data['Date'][:], 
        df_data['VX1Y/VX'][:], 
        label='VX1Y/VIX', c='red'
    )
    line_3M_ratio, = ax2.plot(
        df_data['Date'][:], 
        df_data['VX3M/VX'][:], 
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

    # Create a list of labels to use 
    date_ticks = [ '2022-02-01',
                   '2022-04-01', 
                   '2022-06-02', 
                   '2022-08-01',  
                   '2022-10-03', 
                   '2022-12-01',  
                   ]
    date_labels = ['Feb-22',
                   'Apr-22',
                   'Jun-22',
                   'Aug-22',
                   'Oct-22',
                   'Dec-22',
                   ]

    # Format the axes
    plt.xticks(ticks=date_ticks, labels=date_labels)
    ax1.set_title('SPX vs VIX1Y/VIX')
    ax1.set_ylabel("SPX Closing Marks")
    ax2.set_ylabel('Ratio(s) Closing Marks')
    ax1.set_xlabel('Dates (Month-Year)')
    plt.show()