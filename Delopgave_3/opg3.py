import os
import stat
import csv

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
        with open(data_path, 'r', encoding='utf-8', newline='') as datafile: #we need encoding='utf-8' and newline='' to avoid translation issues when using csv
            with open(res_file, 'w', encoding='utf-8', newline='') as res: #if file exists overwrite it with our dataset - else create new file
                #create csv objects
                datafile_reader = csv.reader(datafile)
                res_writer = csv.writer(res)

                #copy the data
                for row_number, row in enumerate(datafile_reader, start=1):
                    try:
                        if not row: #skip empty rows
                            continue
                        row = [cell.strip() for cell in row] #clean data
                        res_writer.writerow(row)
                    except ValueError as ve:
                        print(f"Value error in row {row_number}: {ve}")
                    except Exception as e:
                        print(f"Unexpected error in row {row_number}: {e}")
        print(f'We have successfully copied the dataset to {res_file}.')
        
    except FileNotFoundError:
        print(f"File not found: {data_path}")
    except PermissionError:
        print(f"Permission denied for file: {data_path} or {res_file}")
    except UnicodeDecodeError:
        print("Could not decode the file – try a different encoding")
    except csv.Error as ce:
        print(f"CSV formatting error: {ce}")
    except OSError as e:
        print(f"OS error occurred during file operations (most likely we have the wrong permissions in the directory): {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")    


if __name__ == '__main__':
    main()