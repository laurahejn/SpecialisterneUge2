
def main():
    """
    sorts and prints the names in the file "Navneliste.txt" from our dataset.
    """
    #please note that this is the local file path - this needs to be changed in order for it run on a different device
    filepath = r"C:\Users\Laura Hejn Brædder\OneDrive - Specialisterne\Dokumenter\SpecialisterneUge2\Data\Navneliste.txt"

    #we use with to ensure that the file is properly closed after use and we give the file shorter name
    with open(filepath) as file:
        names = file.read() #a string containing the content of our file
        namelist = names.split(',') #converts the string "names" into a list by splitting the string at ','
        namelist = [name.strip().lower() for name in namelist] #in order to ensure there is no whitespace on each name and to ensure each name is only in lower cases
        print(namelist)

if __name__ == "__main__":
    main()