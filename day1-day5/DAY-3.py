import pandas as pd

#Creating an empty dataframe
df=pd.DataFrame()
print(df)

print("---------------------")

languages={'Lang':["Python","C++","C","Java"],'Level':["Easy","Medium","Easy","Medium"]}
df=pd.DataFrame(languages)
print(df)

print("---------------------")

#Add remove operations with rows and columns
#Add a row
print("Add a row\n")
newrow=[ "Scala","Hard"]
df.loc[len(df.index)]=newrow
print(df)

print("---------------------")

#Add a column
print("Add a column\n")
df['Downloads']=[150,100,100,100,50]
print(df)

print("---------------------")

#Remove rows
print("Remove a row\n")
df=df.drop(4)
print(df)

print("---------------------")
#Remove Columns
print("Remove a column\n")
df=df.drop('Downloads',axis=1)
print(df)

print("---------------------")
#Indexing the dataframe
#Indexing the rows
print("Indexing the rows\n")
first=df.iloc[[2,3]]
print(first)

print("---------------------")

#Indexing the columns
print("Indexing the columns\n")
first=df['Lang']
print(first)

print("---------------------")
#Naming the index
print("Naming the index\n")
df=pd.DataFrame(df,index=[1,2,3,4])
print(df)

print("---------------------")

#Handling the missing data
print("To check if we have a missing/null data in dataframe")
print(df.isnull().sum())

print("---------------------")

#To drop missing or null values
print("Drop missing data\n")
df=df.dropna(axis=0) # for columns axis will be 1
print(df)

print("---------------------")
#Iterating over rows and columns
print("Iterate rows\n")
for i, j in df.iterrows():
    print(i,j)
    print()

print("---------------------")
print("Iterate columns\n")
for i in df:
    print(df[i])
    print()

print("---------------------")
print("Specific row")
specific=df.loc[df['Level']=='Easy']
print(specific)