import os
import stat

def main():
    '''
    This function should be able to read data from a file and save it in a distination file all the while catching as many errors as possible without crashing the program.
    '''
    #build path to data
    try:
        local_parent = os.getcwd()
    except Exception as e:
        print(f"Failed to get current working directory: {e}")
        return
    relative_data = r'Data\source_data.csv'
    data_path = os.path.join(local_parent, relative_data)

    #check that the data file exists where it is supposed to
    if not os.path.exists(data_path):
        print('The data file does not exists in the given location - please check')
        return
    
    #creating a folder for our result and setting up the right permissions
    res_folder_path = os.path.join(local_parent, 'Delopgave_3', 'res')
    try:
        os.makedirs(res_folder_path, 0o777, exist_ok=True) #to ensure we are able to create new files using open() (grants read, write, execution rights to everyone)
        #notice we use arg exists_ok=True to ensure there is not raised an error in case the directory already exists
        os.chmod(res_folder_path, 0o777) #to overwrite possible umask effects.
    except Exception as e:
        print(f"Failed to create the result folder: {e}")
        return
    
    #check that we have the right permissions
    mode = os.stat(res_folder_path).st_mode
    if stat.S_IMODE(mode) != 0o777:
        print(f'The directory {res_folder_path} does NOT have 777 permissions and we will not be able to create the output file.')

    #read and move data - notice that the 'with open()' corresponds to a try-finally expression
    res_file = os.path.join(res_folder_path, r'copied_data.csv')
    try: 
        with open(data_path, 'r') as datafile:
            with open(res_file, 'a') as res: #if file exists append to it else create and write
                for line in datafile:
                    res.write(line)
        print(f'We have successfully copied the dataset to {res_file}.')
    except OSError as e:
        print(f"OS error occurred during file operations (most likely we have the wrong permissions in the directory): {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()