import os 

def sorted_list(l):
    '''
    This takes a list of strings and sort it lexicographic and then by length
    '''
    l_strip = [element.strip() for element in l] #in order to ensure there is no whitespace on each string 
    l_lex = sorted(l_strip, key = str.lower) #we use the sorted function to sort our list lexicographic and use .lower() to ensure upper and lower case characters are treated equally 
    l_lex_len = sorted(l_lex, key = len) #after the list has been sorted lexicographic we sort it efter the length of each string
    return l_lex_len


def occ_dict(l):
    '''
    This takes a list of strings and makes a dictionary of the frequency of each letter in the alphabet in the list
    '''
    letters = list(map(chr, range(ord('a'), ord('z') + 1))) #this creates a list of all the letters from 'a' to 'z'
    occurrence = [0 for i in range(27)] #this is a list of the occurrence of each letter in all our names - it starts empty
    dict_of_occ = dict(zip(letters, occurrence)) #this is our dictionary of letters and occurrences - right now it is empty-ish
    for elem in l:
        letters_in_elem = list(elem.lower()) #list of characters in name and we ensure that upper case does not matter
        for letter in letters_in_elem:
            dict_of_occ[letter] += 1 #updating the occurrence of the letter by 1
    return dict_of_occ


def main():
    """
    sorts and prints the names in the file "Navneliste.txt" from our dataset an makes a dictionary of the number of occurrence of each letter in the alphabet over all the words in our list.
    """
    #creating the path to our data
    filepath = os.path.join(os.getcwd(), r'Data\Navneliste.txt')

    #we use with to ensure that the file is properly closed after use and we give the file shorter name
    with open(filepath) as file:
        names = file.read() #a string containing the content of our file

    #now that we have created a list of the content of our file we need to sort it    
    namelist = sorted_list(names.split(',')) #converts the string "names" into a list by splitting the string at ',' and running a helper function to sort the list as we want
    
    #now we need to create a dictionary counting the occurrence of each letter in all the names
    dict_of_occ = occ_dict(namelist)

    return namelist, dict_of_occ
    

if __name__ == "__main__":
    namelist, dict_of_occ = main()
    for name in namelist:
        print(name)
    print(dict_of_occ)