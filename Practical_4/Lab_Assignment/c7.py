import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Pre-processing 
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)

# One-hot encoding 
# Using dtype=int or astype(int) ensures we get 1/0 instead of True/False
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Survival rate by class
print(data.groupby('Pclass')['Survived'].mean())

# 2. Survival rate by Embarked_S
print(data.groupby('Embarked_S')['Survived'].mean())

# 3. Survival rate by family size
print(data.groupby('FamilySize')['Survived'].mean())

# 4. Survival rate by being alone
print(data.groupby('IsAlone')['Survived'].mean())

# 5. Average fare by class
print(data.groupby('Pclass')['Fare'].mean())

# 6. Average age by class (DO NOT fill NaNs before this)
print(data.groupby('Pclass')['Age'].mean())

# 7. Average age by survival status
print(data.groupby('Survived')['Age'].mean())

# 8. Average fare by survival status
print(data.groupby('Survived')['Fare'].mean())

# 9. Number of survivors by class
survivors = data[data['Survived'] == 1]
print(survivors['Pclass'].value_counts())

# 10. Number of non-survivors by class
non_survivors = data[data['Survived'] == 0]
print(non_survivors['Pclass'].value_counts())