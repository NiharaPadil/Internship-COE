import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

dataset=pd.read_csv('C:/Users/sanks/Sahyadri/Internships/Internship-II/DATASETS/ONLINEFRAUD.csv')

#Describe the dataset

print(dataset.describe())
print(dataset.info())

#Univariate analysis means analysing the single variable which mean
#we can analyse it using plots such as histogram,boxplot,density plots which uses single variable
#Histogram
plt.hist(dataset['amount'])
plt.show()

#Boxplot
plt.boxplot(dataset['amount'])
plt.show()

#Bivariate analysis means analysing two variables of a dataset and
#Representing it using plots such as scatter,line bar etc which uses 2 variables
#Scatter plot
plt.scatter(dataset['isFraud'],dataset['isFlaggedFraud'])
plt.show()

#Line plot
plt.plot(dataset['oldbalanceOrg'],dataset['newbalanceOrig'])
plt.show()

#Fetch the basic information
print(dataset.info())

#Missing and null values
mv=dataset.isnull()
print(mv)
mc=mv.sum()
print(mc)

#Replace the null values
dataset.fillna(0,inplace=True)
print(dataset)

dataset=dataset.dropna(axis=0) #To drop missing or null values
print(dataset)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame({'name': ['Adi','ravi','neethu','tarun'],
                     'marks': [25,35,50,45]})
# data = pd.read_csv('F:/internship/dataframe.xlsx')
plt.figure(figsize=(15, 5))
sns.barplot(x=data['name'], y=data['marks'],data=data)
plt.xlabel('name')
plt.ylabel('marks')
plt.title('Barplot')
plt.show()


# basic info
print('Basic info')
data.info()
print('-----------------------------------------------------------------------------------------------')
# Get the count of quantitative, qualitative, nominal, categorical data if any
print('Get the count of quantitative, qualitative, nominal, categorical data if any')
quan = 0
quali= 0
nom = 0
categ=0

for column in data.columns:
    if data[column].dtype in ['int64', 'float64']:
        quan += 1
    else:  # Non-numeric data types
        quali += 1
        unique_values = len(data[column].unique())
        if unique_values > 2:
            nom += 1
        else:
            categ += 1

print("Quantitative")
print(quan)
print("Qualitative")
print(quali)
print("Nominal data count")
print(nom)
print("Catagorical datacount")
print(categ)


print('-----------------------------------------------------------------------------------------------')

#Display the descriptive statics
print('Display the descriptive statics')
all_stats = data.describe(include='all')
print(all_stats)

print('-----------------------------------------------------------------------------------------------')
#Check for duplicate values
print('Check for duplicate values')
duplicate_rows = data[data.duplicated()]

print('-----------------------------------------------------------------------------------------------')
print("Duplicate Rows:")
print(duplicate_rows)


data_no_duplicates = data.drop_duplicates()

print("Dataset without duplicates:")
print(data_no_duplicates)


print('-----------------------------------------------------------------------------------------------')
# Know the unique values in particular column
print('Know the unique values in particular column')
unique_values = data['name'].unique()
print("Unique values in 'Name':")
print(unique_values)


print('-----------------------------------------------------------------------------------------------')

# Know data types of all attribute
print('Know data types of all attribute')
column_data_types = data.dtypes

print("Data Types of All Attributes:")
print(column_data_types)




























