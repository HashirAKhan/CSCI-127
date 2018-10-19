#Name: Hashir Khan
#Date: October 18th, 2018
#This assignment modifys the floodmap
import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = .25
        elif elevations[row,col] % 10 == 0:
            floodMap[row,col,0] = 0
            floodMap[row,col,0] = 0
            floodMap[row,col,0] = 0
        else:
            floodMap[row,col,0] = .5
            floodMap[row,col,1] = .5
            floodMap[row,col,2] = .5
plt.imshow(floodMap)
plt.show()
plt.imsave('floodMap.png',floodMap)
