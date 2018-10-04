#Name: Hashir Khan
#Date: September 25, 2018
#This program make a picture blue

import matplotlib.pyplot as plt
import numpy as np

start = input("Enter name of the input file: ")
end = input("Enter name of the output file: ")

img = plt.imread(start)
plt.imshow(img)
plt.show()

start2 = img.copy()
start2[:,:,0] = 0
start2[:,:,1] = 0

plt.imshow(start2)
plt.show()

plt.imsave(end, start2)
