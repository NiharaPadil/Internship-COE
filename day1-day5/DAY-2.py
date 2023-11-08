import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data=pd.read_csv('C:/Users/sanks/Sahyadri/Internships/Internship-II/DATASETS/DAY-2_Small_Dataset.csv')

values=data['Weight']

print(values)

mean=np.mean(values)

median=np.median(values)

mode=stats.mode(values)

max=np.max(values)
min=np.min(values)
range=max-min

standarddev=np.std(values)

variance=np.var(values)

print(f"The mean is: {mean}")

print(f"The median is: {median}")

print(f"The mode is: {mode}")

print(f"The range is: {range}")

print(f"The standard deviation is: {standarddev}")

print(f"The variance is: {variance}")

#Draw a bar graph with all values of weight and mean
plt.figure(figsize=(8, 6))
plt.bar(values.index, values, label='Column Values')
plt.axhline(mean, color='red', linestyle='dashed', label='Mean')
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('Bar Graph of Column Values with Mean')
plt.legend()
plt.show()