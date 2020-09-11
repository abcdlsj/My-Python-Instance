import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

students = pd.read_csv('./ucdavis.csv')
g = sns.FacetGrid(students,hue="gender",palette="Set1",size=10)
g.map(plt.scatter,"gpa","computer",s=100,linewidth=0.65,edgecolor="white")

g.add_legend()