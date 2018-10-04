#Name: Hashir Khan
#Date: September 25, 2018
#This program counts the number of Gs and Cs in DNA sequence
x = input("Please enter a DNA sequence: ")
count = len(x)
print(count)
gc = x.count("C")+x.count("G")
print ("GC-content is " + str(gc/count))
