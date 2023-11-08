import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import seaborn as sns

# 1.	Filter the data based on some logic
print('1.	Filter the data based on some logic')
df=pd.read_csv('C:/Users/sanks/Sahyadri/Internships/Internship-II/DATASETS/ONLINEFRAUD.csv')
df = df.head(10)

filtered = df[df['amount']>5000]
output = 'filterd.csv'
filtered.to_csv(output,index=False)
df2=pd.read_csv('C:/Users/sanks/Sahyadri/Internships/Internship-II/ONLINEFRAUD.csv')
print(df2)

print('---------------------------------------------------------------------------------------------------')
#2
# Rename the columns if required
print('Rename the columns if required')
df=pd.read_csv('C:/Users/sanks/Sahyadri/Internships/Internship-II/ONLINEFRAUD.csv')
column_mapping = {
    'amount': 'newamt'
}
df.rename(columns=column_mapping, inplace=True)
print(df)
print('---------------------------------------------------------------------------------------------------')

#3a
x=df['oldbalanceOrg']
y=df['newbalanceOrig']
corr_coefficient, _ = scipy.stats.pearsonr(x, y)
plt.scatter(x, y, label=f'Correlation = {corr_coefficient:.2f}', color='b')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.legend()
plt.show()

# 4.	Drop the irrelevant columns
df.drop(columns=['newamt'], inplace=True)
print(df)

#5
print(df['type'].unique())


# 6.Detect outliers
sns.boxplot(data=df, orient="h")
plt.title("Boxplot with Outliers")
plt.xlabel("Values")
plt.show()


#7
print(df.dtypes)

print("Corre")
