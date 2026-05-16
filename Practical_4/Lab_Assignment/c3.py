import pandas as pd

# Prompt the user for the file name
# Note: input() with no prompt matches the "Actual output" style 
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# 1. Group by 'City' and calculate the total 'Quantity' for each city
city_totals = df.groupby('City')['Quantity'].sum()

# 2. Find the city that sold the most products
# idxmax() returns the label (index) of the maximum value
best_city = city_totals.idxmax()

# Display the result
print(f"City sold the most products: {best_city}")
