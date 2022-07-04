#Vowel count using python

from itertools import count


def vowel_count(str):
    # set count=0 for initials
    count = 0
    # set the vowel alphabet
    vowel = set("aeiouAEIOU")
    #for
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print("No of vowels: ",count)
    
str="Geekforgeeks"
vowel_count(str)
