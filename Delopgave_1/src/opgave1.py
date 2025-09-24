
def main():
    """
    sorts and prints the names in the file "Navneliste.txt" from our dataset an makes a dictionary of the number of occurrence of each letter in the alphabet over all the words in our list.
    """
    #please note that this is the local file path - this needs to be changed in order for it run on a different device
    filepath = r"C:\Users\Laura Hejn Brædder\OneDrive - Specialisterne\Dokumenter\SpecialisterneUge2\Data\Navneliste.txt"

    #we use with to ensure that the file is properly closed after use and we give the file shorter name
    with open(filepath) as file:
        names = file.read() #a string containing the content of our file

    #now that we have created a list of the content of our file we need to sort it    
    namelist = names.split(',') #converts the string "names" into a list by splitting the string at ','
    namelist = [name.strip() for name in namelist] #in order to ensure there is no whitespace on each name 
    namelist = sorted(namelist, key = str.lower) #we use the sorted function to sort our namelist lexicographic and use .lower() to ensure upper and lower case characters are treated equally 
    namelist = sorted(namelist, key = len) #after the list has been sorted lexicographic we sort it efter the length of each string
    
    #we print the sorted list of names
    for name in namelist:
        print(name)
    
    #now we need to create a dictionary counting the occurrence of each letter in all the names
    letters = list(map(chr, range(ord('a'), ord('z') + 1))) #this creates a list of all the letters from 'a' to 'z'
    occurrence = [0 for letter in letters] #this is a list of the occurrence of each letter in all our names - it starts empty
    dict_of_occ = dict(zip(letters, occurrence)) #this is our dictionary of letters and occurrences - right now it is empty-ish
    for name in namelist:
        letters_in_name = list(name.lower()) #list of characters in name and we ensure that upper case does not matter
        for letter in letters_in_name:
            dict_of_occ[letter] += 1 #updating the occurrence of the letter by 1
    
    print(dict_of_occ)
    

if __name__ == "__main__":
    main()