#Name Hashir Khan
#Date October 19th, 2018
#This program displays the fraction of the population that lived in a borough, over time
import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input('enter a borough: ')
name = input('enter a name for the output file')
pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(name)
