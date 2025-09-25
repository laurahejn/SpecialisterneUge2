import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import pandas as pd
import opgave1

def freq_analysis(d):
    """
    Takes as input a dictionary of letters and their occurrence and returns a dictionary of the frequence of each letter - here we intepret it as the relative frequence since we already have to total frequence in the dictionary of exercise 1.
    """
    sum_of_letters = sum(d.values())
    keys = list(map(chr, range(ord('a'), ord('z') + 1)))
    freq = [value/sum_of_letters*100 for value in d.values()]
    freq_dict = dict(zip(keys, freq)) #this is our relative frequency dictionary
    
    #makes a histogram of the frequency of letters
    plt.bar(keys, freq, color='DarkRed', edgecolor='black')
    plt.xlabel('Letters')
    plt.ylabel('Frequency in %')
    plt.title('Letter frequency in Navneliste.txt')
    plt.show()
    return freq_dict


def wordcl(d):
    '''
    Takes a dictionary of frequences as input and makes a wordcloud of the letters where the more frequent a letter is the larger it appears in the cloud.
    '''
    wordcloud = WordCloud(width = 800, height = 400, background_color = "white", colormap = 'magma').generate_from_frequencies(d)

    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Frequency of letters in the names')
    plt.show()


def stat_analysis(l):
    '''
    Find median and mean of the length of the elements in a list and presents it in a boxplot
    '''
    len_l = [len(elem) for elem in l] #makes a list of the length of each element in the given list (notice that our list is already sorted)
    numbers_of_elem_in_l = len(l)
    #first we find the median of the list - notice that this could also be done by using the package 'statistics' and its function 'median'
    #if the length of the list is even and we define the median as the average of the two numbers in the middle else the median is defined as the number in the middle position of the list 
    #(and if the list if ueven the element at mid_pos is the same from both the right and the left)
    mid_pos = numbers_of_elem_in_l // 2
    median = (len_l[mid_pos] + len_l[-mid_pos]) / 2
    print('The median of the length of names is {}'.format(median))
    
    #now for the mean
    mean = sum(len_l) / numbers_of_elem_in_l
    print('The mean of the length of names is {}'.format(mean))

    #the visualization by a boxplot
    df = pd.DataFrame(list(zip(l, len_l)), columns=['names', 'name length'])
    sns.catplot(data = df, x='name length', kind='box')
    plt.show()


def remove_dupl(l):
    '''
    Removes duplicates from a list by converting it to a set and the returns the list without duplicates
    '''
    return list(set(l))


def analysis(namelist, dict_of_occ):
    #first we run our frequency analysis
    freq_dict = freq_analysis(dict_of_occ)
    #then we make a word cloud
    wordcl(freq_dict) #notice that dict_of_occ also would work perfectly fine here
    #and now for the name length analysis
    stat_analysis(namelist)


def main():
    """
    This function runs all our visualization functions.
    """
    namelist, dict_of_occ = opgave1.main()
    analysis(namelist, dict_of_occ)

    #then run it again but where we remove any duplicates
    namelist_nodupl = opgave1.sorted_list(remove_dupl(namelist))
    dict_of_occ_nodupl = opgave1.occ_dict(namelist_nodupl)
    if namelist == namelist_nodupl:
        print('there are no duplicates in the namelist')
    else:
        analysis(namelist_nodupl, dict_of_occ_nodupl)

    


if __name__ == "__main__":
    main()