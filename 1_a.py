import pandas as p
import numpy as n
data=[197,199,234,267,269,276,281,289,299,301,339] # list of numbers for which box plot is plotted and outliers are determined 
outliers=[] # initialising list for outliers 
d=p.DataFrame(data) # converting list to data frame 
boxplot=d.boxplot() # initialising box plot object 
Q1, Q3= n.percentile(data,[25,75]) #Determining the quartiles with percentile function 
print("Q1: ",Q1)
print("Q3: ",Q3)
IQR=Q3-Q1 # calculate inter quartile ranges
print("IQR: ",IQR)
lower_bound = Q1 -(1.5 * IQR) # calculate lower bound of box plot
upper_bound = Q3 +(1.5 * IQR) # calculate upper bound of box plot
print("lower_bound: ",lower_bound)
print("upper_bound: ",upper_bound)
for i in data: # for all the data check if any data is out the range of lower bound and upper bound to determine outliers
    if i>upper_bound or i<lower_bound:
        outliers.append(i) 
print("outliers: ",outliers) 
