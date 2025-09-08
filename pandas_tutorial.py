# Pandas - Dataframe and Series
## Pandas is a powerful data manipulation library in python, widely used for data analysis and data cleaning. It consists of two primary data structures: Series and Dataframe. 

## Series - A series is a one-dimensional array like object that can hold any data type. It is similar to a column in a table. 

## Dataframes - While a dataframe is a 2D, size-mutable and potentially heterogeneous tabular data structure with labeled axes (rows and columns). 

# How to install Pandas?
## Using cmd - `pip install pandas`
## Using colab/jupyter - `!pip install -q pandas`

# Import the pandas library
import pandas as pd 

# Check the pandas version
# print(pd.__version__)

## Creating a series using list
# data = [1,2,3,4,5]

# series = pd.Series(data)

# print("Series \n",series)

## Creating a series from dictionary

# data = {"a" : 1, "b" : 2, "c" : 3}
# series_dict = pd.Series(data)
# print(series_dict)

# values = [10,20,30]
# indexes = ["naruto", "sky", "alya"]

# data_series = pd.Series(data=values,index=indexes)

# print(data_series)

## Dataframes
## Create a data frame from a dictionary of lists

# data = {
#   'Name' : ['Abhi', 'Alya', 'Vaani', 'Naruto'],
#   'Age' : [25, 17, 25, 17],
#   'Country' : ['Japan', 'Japan', 'India', 'Japan']
# }

# df = pd.DataFrame(data=data)

# print(df)
# print(type(df))

## Create a Dataframe from a list of dictionaries 
# data = [
#   {'Name' : 'Abhi', 'Age' : 25, 'Country' : 'Japan'},
#   {'Name' : 'Alya', 'Age' : 17, 'Country' : 'Japan'},
#   {'Name' : 'Vaani', 'Age' : 25, 'Country' : 'India'}
# ]

# df = pd.DataFrame(data=data)

# print(df)
# print(type(df))

PATH = r'students.csv'

df = pd.read_csv(PATH)

## Top 5 record in my dataframe
# print(df.head())

##  Bottom 5 record in my dataframe
# print(df.tail())

## Access a particular column
# print(type(df['name']))

## We use df.loc[index] to locate a particular row based on row indexes.
# print(df.loc[0])

## We use df.iloc[index] to locate a particular element based on indexes.
# print(df.iloc[0][0])

## Accessing a specified element
# print(df.at[1,'age'])


## Accessing specified element using iat. 
# print(df.iat[2,1])

## Data manipulation with Dataframe. 
import random 

scores = list(tuple(range(1,101)))

random.shuffle(scores)

## Adding a column
df['score'] =  scores 

# print(df.head())
# print("*"*32)
## Remove a column
## axis = 0 (row)
## axis = 1 (column)
## inplace = True (means permanent deletion)

# df.drop('age',axis=1,inplace=True)

# print(df.head())
# print("*"*32)

# print(df.head())
# print("*"*32)

# df['age'] = df['age'] + 100 
# print(df.head())

## Display the data types of each columns
# print("Data Types:\n",df.dtypes)
# print("*"*32)

## Display all the various different column names
# print("Column Names:\n",df.columns)
# print("*"*32)

## Describe the dataframe 
## Generally it shows the statistical information about the numerical columns only. 

# print("Statistical summary:\n", df.describe())

## We can also transpose the above table. 
# print("Statistical summary:\n", df.describe().T)

## We can also view the object(strings) statistical information. 
## Object type in Pandas dataframe
## Object : The object data type is like a mixed bag or a text box — it usually stores words and letters (strings), but it can also hold other things that don’t fit neatly as numbers.
## It means that anything other than numbers (int and float) and boolean values are considered as 
## objects. 

# print("Statistical summary:\n", df.describe(include='object'))

## View the information of the dataframe using `df.info()`
## It will tell you:
## Column names (like “Name”, “Age”, “Passed”).
## How many rows are filled (non-null = not empty).
## What type of data is in each column (int64, float64, object, bool, etc.).
## Also, it tells us how many columns belong to each data type.
## How much memory the DataFrame is using in your computer’s RAM.
## None
## → This appears because you used print(df.info()).

## `df.info()`` already prints the info itself. Since it doesn’t return anything, Python prints None.

# print(df.info())

## Counting how many times each thing is repeated in a column.
## We use df['column_name'].value_counts()
## value_counts() is like asking pandas:
## 👉 “Hey, tell me how many times each item appears in this column!”

print(df['grade'].value_counts())