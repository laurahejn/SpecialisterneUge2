import os


def get_path(local_path, relative_path):
    return os.path.join(local_path, relative_path)

def add_folder_for_res(local_path, rel_end_loc, name):
    path = os.path.join(local_path, os.path.join(rel_end_loc, name))
    os.makedirs(path)


def main():
    """
    What runs when
    """
    #first we have our data
    local_parent = os.getcwd()
    relative_data = r'Data\app_log (logfil analyse) - random.txt'
    data_dir = get_path(local_parent, relative_data)

    with open(data_dir, 'r') as datafile:
        for line in datafile:
            None

    #then we need a folder for the result files
    #add_folder_for_res(local_parent, 'Delopgave_2', 'results')

    


if __name__ == "__main__":
    main()