# https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/
from pylab import *

import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("train.csv") #Reading the dataset in a dataframe using Pandas\

#Write on IPython console
df.head(10)     #first 10 rows
df.describe()   #summary of numerical variables
df['Property_Area'].value_counts() #Frequency distribution
df['ApplicantIncome'].hist(bins=50) # hist explanation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
df.boxplot(column='ApplicantIncome') # Box plot
df.boxplot(column='ApplicantIncome', by = 'Education') # Segregate income with Education
