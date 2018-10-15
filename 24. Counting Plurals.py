#Name: Hashir Khan
#Date: October 17th, 2018
#This program tells you the ratio of plural nouns
words = input("enter nouns: ")
nouns = words.split(' ')
print("Number of words: " + str(len(nouns)))
count = 0
for i in nouns:
    if i[-1]=='s':
        count+=1
print("Fraction of your list that is plural is " + str(count/len(nouns)))
