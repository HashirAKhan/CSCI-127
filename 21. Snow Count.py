#Name: Hashir Khan
#Date: October 11th, 2018
#This program loads an image, counts the number of pixels that are
#    nearly white as an estimate for snow pack.
import matplotlib.pyplot as plt
import numpy as np
x = input("Enter the name of the image")
ca = plt.imread(x)
countSnow = 0            
t = 0.75                 
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow += 1
print("Snow count is", countSnow)
