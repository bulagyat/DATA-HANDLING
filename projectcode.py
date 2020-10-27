import numpy as np
import pandas as pd
import os

#use pip install pandas

data = pd.read_csv(os.getcwd() + "\Desktop\Big Data\MOCK_DATA (1).csv", delimiter=',')
# print(data.head()) # ----> displays first 5 rows, useful for checking if loaded correct data or not
# print('')
# print(data.tail()) # ----> displays last 5 rows, useful for checking if loaded correct data or not

# Data filtering ---> indexing or positioning
print("DATA FILTERING")
print (data[data.Region == 'Asia'])
# print (data[data.Region == 'Asia'].sum())
# # print('')
# # print (data[data.Gender == 'Female'].head(10))
# # print('')
# # print (data[data.Gender == 'Female'].tail(10))
# # #data[data.column == 'whatever you want to see'] ---> general command syntax if you want to sort it out through the columns

# #Group by ---> sorting by coulumns
print("GROUPBY")
print(data.groupby('Gender').count())
print(data.groupby('Region').count())
# print(data.groupby('Department').count())

# #Average 2 ways 1. groupby command 
# print("AVERAGE")
# print(data.groupby('Gender').mean()[['Age']]) # ---> average for a specific class (line 28, 29 same concept)
# print('')
# print(data.groupby('Department').mean()[['Salary']]) # ---> average for a specific class
# print('')
# print("Average salary is:", data['Salary'].mean()) # ---> average salary (no group by) so for the general database as a whole

# #Sorting ---> 2 types, ascending and descending
# print("SORTING")
# print(data.sort_values('Salary')) # ---> ascending
# print('')
# print(data.sort_values('Name'))
# print('')
# print(data.sort_values('Salary', ascending=[False])) # ---> descending

# #Combination Sorting and Groupby
# print("COMBI SORT GROUPBY")
# print(data.sort_values('Salary').groupby('Department'))
# print('')
# print(data.sort_values('Salary').groupby('Department').head(8))
# print('')
# print(data.sort_values('Salary').groupby('Department').head(10))
# print('')
# print(data.sort_values('Name', ascending=[False]).groupby('Department').head(10))