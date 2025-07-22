Here are 10 basic interview questions on Pandas—commonly asked in data engineering, data analysis, and Python interviews—along with short sample answers or code snippets:

✅ 1. What is Pandas in Python?
Answer:

Pandas is an open-source Python library used for data manipulation and analysis. It provides two primary data structures:

Series: 1D labeled array

DataFrame: 2D labeled data structure (like a table)

✅ 2. How to create a DataFrame in Pandas?

import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)


✅ 3. How do you read a CSV file using Pandas?

df = pd.read_csv('filename.csv')


✅ 4. How to get the top 5 rows of a DataFrame?

df.head()


✅ 5. How to get basic statistics (mean, std, count, etc.) for numeric columns?

df.describe()


✅ 6. How do you filter rows based on a condition?

df[df['Age'] > 25]


✅ 7. How to handle missing values in a DataFrame?

df.fillna(0)          # Replace missing values with 0  
df.dropna()           # Drop rows with missing values
df.isnull().sum()     # Count missing values per column


✅ 8. How do you add a new column to a DataFrame?

df['Salary'] = [50000, 60000]


✅ 9. How to group data and find the average per group?

df.groupby('Department')['Salary'].mean()


✅ 10. How to sort a DataFrame by a column?

df.sort_values(by='Age', ascending=False)


✅ 11. How do you merge two DataFrames?

pd.merge(df1, df2, on='id', how='inner')
You can also use left, right, or outer joins.

✅ 12. What is the difference between loc[] and iloc[]?
loc[] is label-based (uses column/row names)

iloc[] is index-based (uses integer positions)

df.loc[0, 'Name']   # By label
df.iloc[0, 0]       # By index


✅ 13. How do you apply a custom function to a column?

df['Age_plus_5'] = df['Age'].apply(lambda x: x + 5)


✅ 14. How to remove duplicates from a DataFrame?

df.drop_duplicates()


✅ 15. What is a pivot table in Pandas?
Used to reshape and summarize data.

df.pivot_table(index='Department', values='Salary', aggfunc='mean')


