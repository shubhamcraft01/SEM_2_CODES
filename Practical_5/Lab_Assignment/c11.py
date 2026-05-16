import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Scatter Plot for Age vs. Fare by Survived
# Scatter plot with color mapping
colors = data['Survived'].map({0: 'red', 1: 'blue'})

plt.scatter(data['Age'], data['Fare'], c=colors)

# Title and labels
plt.title("Age vs. Fare by Survival")
plt.xlabel("Age")
plt.ylabel("Fare")

# Show plot
plt.show()


