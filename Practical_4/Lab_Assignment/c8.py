import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Pre-processing: One-hot encode Embarked to get Embarked_S
# We cast to int to ensure we get 0/1 instead of True/False
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Get the number of survivors by gender (Sex)
survivors = data[data['Survived'] == 1]
print(survivors['Sex'].value_counts())

# 2. Get the number of non-survivors by gender (Sex)
non_survivors = data[data['Survived'] == 0]
print(non_survivors['Sex'].value_counts())

# 3. Get the number of survivors by embarkation location (Embarked_S)
print(survivors['Embarked_S'].value_counts())

# 4. Get the number of non-survivors by embarkation location (Embarked_S)
print(non_survivors['Embarked_S'].value_counts())

# 5. Calculate the percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
print(children['Survived'].mean())

# 6. Calculate the percentage of adults (Age >= 18) who survived
adults = data[data['Age'] >= 18]
print(adults['Survived'].mean())

# 7. Get the median age of survivors
# Note: Pandas median() ignores NaN values automatically
print(survivors['Age'].median())

# 8. Get the median age of non-survivors
print(non_survivors['Age'].median())

# 9. Get the median fare of survivors
print(survivors['Fare'].median())

# 10. Get the median fare of non-survivors
print(non_survivors['Fare'].median())
