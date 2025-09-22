import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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

def opg1():
    """
    sorts and prints the names in the file "Navneliste.txt" from our dataset an makes a dictionary of the number of occurrence of each letter in the alphabet over all the words in our list.
    """
    #please note that this is the local file path - this needs to be changed in order for it run on a different device
    filepath = r"C:\Users\Laura Hejn Brædder\OneDrive - Specialisterne\Dokumenter\SpecialisterneUge2\Data\Navneliste.txt"

    #we use with to ensure that the file is properly closed after use and we give the file shorter name
    with open(filepath) as file:
        names = file.read() #a string containing the content of our file

    #now that we have created a list of the content of our file we need to sort it    
    namelist = sorted_list(names.split(','))
    
    #now we need to create a dictionary counting the occurrence of each letter in all the names
    dict_of_occ = occ_dict(namelist)
    
    return namelist, dict_of_occ


def freq_analysis(d):
    """
    Takes as input a dictionary of letters and their occurrence and returns a dictionary of the frequence of each letter.
    """
    sum_of_letters = sum(d.values())
    freq = dict(zip(list(map(chr, range(ord('a'), ord('z') + 1))), [value/sum_of_letters for value in d.values()])) #this is our frequency dictionary
    
    plt.hist(d.keys(), d.values(), color = "DarkRed") #makes a histogram of the frequency of letters

    return freq

def wordcl(l):
    '''
    Takes a list of names as input and makes a wordcloud of the letters where the more frequent a letter is the larger it appears in the cloud.
    '''
    list_of_letters = []
    for elem in l:
        for letter in elem.lower():
            list_of_letters.append(letter)
    wordcloud = WordCloud(width = 800, heigth = 400, background_color = "white", colormap = 'magma').generate(list_of_letters)

    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Frequency of letters in the names')
    plt.show()

def remove_dupl(l):
    '''
    Removes duplicates from a list by converting it to a set and the returns the list without duplicates
    '''
    return list(set(l))

def main():
    """
    This function runs all our visualization functions.
    """
    namelist, dict_of_occ = opg1()

    #first we run our frequency analysis
    freq = freq_analysis(dict_of_occ)
    wordcl(namelist)


if __name__ == "__main__":
    main()