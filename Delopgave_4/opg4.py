import pandas as pd
import matplotlib.pyplot as plt
import os

def grp_hist_plot(df, group_by, target_mean):
    '''
    This function makes a histogram of the mean value of the column 'target_mean' in the dataframe 'df' grouped by 'group_by'.
    '''
    grp = df.groupby(by = group_by)[target_mean].mean()
    grp.plot(kind = 'bar', xlabel = 'group', ylabel = 'mean')
    plt.title('The mean of {}'.format(target_mean))
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

    #The of the purchase price grouped by the house type
    grp_hist_plot(df, 'region', 'purchase_price')

    #plotting the house_type
    grp_hist_plot(df, 'house_type', 'sqm_price')



if __name__ == "__main__":
    main()