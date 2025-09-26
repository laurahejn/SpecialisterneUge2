import pandas as pd
import matplotlib.pyplot as plt
import os

def grp_hist_plot(df, group_by, target_mean, kind='bar'):
    '''
    This function makes a histogram of the mean value of the column 'target_mean' in the dataframe 'df' grouped by 'group_by'.
    '''
    grp = df.groupby(by = group_by)[target_mean].mean()
    grp.plot(kind = kind, xlabel = 'group', ylabel = 'mean')
    plt.title('The mean of {}'.format(target_mean))
    plt.tight_layout()
    plt.show()

def grp_counter_plot(df, grp_by, kind='bar'):
    count = df[grp_by].value_counts()
    count.plot(kind=kind)
    plt.title('Number of occurences of {}'.format(grp_by))
    plt.tight_layout()
    plt.show()



def main():
    """
    Function that goes through log file and results in the creation of a new folder that contains a file for each type of log entrence and each file then contains all the logs of this type in the original log file.
    """
    #first we have our data
    local_parent = os.getcwd()
    relative_data = r'Data\DKHousingPricesSample100k.csv'
    data_path = os.path.join(local_parent, relative_data)

    #read the csv file into a DataFrame
    df = pd.read_csv(data_path)

    #printing the first 10 rows
    print('The first 10 rows in our dataset.')
    print(df.head(10))

    #The of the mean of purchase price grouped by region
    grp_hist_plot(df, 'region', 'purchase_price')

    #plotting the mean of the square meter price grouped by house_type
    grp_hist_plot(df, 'house_type', 'sqm_price')

    #plotting the mean of rates grouped by first region and then house type
    grp_hist_plot(df, ['region', 'house_type'], ['nom_interest_rate%', 'dk_ann_infl_rate%', 'yield_on_mortgage_credit_bonds%'])

    #counter plot
    grp_counter_plot(df, 'house_type', 'pie')


if __name__ == "__main__":
    main()