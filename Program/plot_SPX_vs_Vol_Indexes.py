# Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt

def plot_SPX_vs_vol_indexes(data_file):
# Create a dataframe using the data from the csv file
    df_data = pd.read_csv(data_file)

    # Create a plot & Declare first axis
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Create lines for VIX Ratios
    line_spx, = ax1.plot(
        df_data['Date'], 
        df_data['SPX_Close'], 
        label='SPX'
        )
    line_9D_index, = ax2.plot(
        df_data['Date'][:], 
        df_data['9D_Close'][:], 
        label='VX9D', c='red'
        )
    line_vx_index, = ax2.plot(
        df_data['Date'][:], 
        df_data['vx_Close'][:], 
        label='VIX', c='green'
        )
    line_3M_index, = ax2.plot(
        df_data['Date'][:], 
        df_data['3M_Close'][:], 
        label='VX3M', c='orange'
        )
    line_6M_index, = ax2.plot(
        df_data['Date'][:], 
        df_data['6M_Close'][:], 
        label='VX6M', c='olive'
        )
    line_1y_index, = ax2.plot(
        df_data['Date'][:], 
        df_data['1Y_Close'][:], 
        label='VX1Y', c='dimgrey'
        )


    # Plot lines & format figure
    # Format and create legend
    fig.legend(
        (line_spx, 
         line_9D_index, 
         line_vx_index, 
         line_3M_index, 
         line_6M_index, 
         line_1y_index,
         ), 
        ('SPX',
         'VIX 9D', 
         'VIX', 
         'VIX 3M',
         'VIX 6M',
         'VIX 1Y',
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
    ax1.set_title('SPX vs VIX Indicies')
    ax1.set_ylabel("SPX Closing Marks")
    ax2.set_ylabel('VIX Index Closing Marks')
    ax1.set_xlabel('Dates (Month-Year)')
    plt.show()