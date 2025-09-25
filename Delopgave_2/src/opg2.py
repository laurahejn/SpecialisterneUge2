import os

def main():
    """
    Function that goes through log file and results in the creation of a new folder that contains a file for each type of log entrence and each file then contains all the logs of this type in the original log file.
    """
    #first we have our data
    local_parent = os.getcwd()
    relative_data = r'Data\app_log (logfil analyse) - random.txt'
    data_path = os.path.join(local_parent, relative_data)

    #creating a folder for our log analysis and setting up the right permissions
    res_folder_path = os.path.join(local_parent, r'Delopgave_2\res')
    os.makedirs(res_folder_path, 0o777) #to ensure we are able to create new files using open() (grants read, write, execution rights to everyone)

    #log analysis
    with open(data_path, 'r') as datafile: 
        for line in datafile:
            line_list = line.split() #split line at whitespace
            log_type = line_list[2] #the first two entries is the date and the time of the log - then the log type
            underlog = os.path.join(res_folder_path, r'{}.txt'.format(log_type))
            with open(underlog, 'a') as textfile: #if file exists append to it else create and write
                textfile.write(line)
                


if __name__ == "__main__":
    main()