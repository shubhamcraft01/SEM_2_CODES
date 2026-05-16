import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Pre-requisite from previous part
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)
data['IsAlone'] = np.where(data['FamilySize'] == 0, 1, 0)

# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode the ‘Embarked' column
# drop_first=True helps avoid the dummy variable trap
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4. Get the mean age of passengers
mean_age = data['Age'].mean()
print(mean_age)

# 5. Get the median fare of passengers
median_fare = data['Fare'].median()
print(median_fare)

# 6. Get the number of passengers by class
print(data['Pclass'].value_counts())

# 7. Get the number of passengers by gender (0 for male, 1 for female)
print(data['Sex'].value_counts())

# 8. Get the number of passengers by survival status
print(data['Survived'].value_counts())

# 9. Calculate the survival rate of passengers
survival_rate = data['Survived'].mean()
print(survival_rate)

# 10. Calculate the survival rate by gender
survival_rate_by_gender = data.groupby('Sex')['Survived'].mean()
print(survival_rate_by_gender)

