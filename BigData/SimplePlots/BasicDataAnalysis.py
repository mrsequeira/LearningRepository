# -*- coding: utf-8 -*-
"""
Spyder Editor

Ref:https://users.physics.unc.edu/~sheila/pythontutorial.html
"""
import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt(r"<Directorie-To-TestDatafile>") 

print(data)

temperature=data[:,0] 
humidity=data[:,1] 
plt.plot(humidity,temperature) #Simple plot
plt.plot(humidity,temperature,'b.',markersize=12) #Blue dots size 12
#add axis labels and a title
plt.title('Fantastic Plot #1')
plt.xlabel('humidity (%)')
plt.ylabel('temperature (F)')
#change the axis ranges
plt.xlim(10,60)
plt.ylim(75,100)
#Visualize range of values changing dot size and form
sel2=np.where((temperature > 80) & (temperature < 90))
plt.plot(humidity[sel2],temperature[sel2],'g*',markersize=15)