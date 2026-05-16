import pandas as pd

# 1. Prompt the user for the file name
file_name = input()

# 2. Load the data
df = pd.read_csv(file_name)

# 3. Group by Product and sum the quantities
# This creates a Series where Products are indices and values are the total quantities
product_totals = df.groupby("Product")["Quantity"].sum()

# 4. Find the product name (index) with the highest quantity
best_product = product_totals.idxmax()

# 5. Find the actual quantity (value) for that product
highest_quantity = product_totals.max()

# 6. Display the result exactly as per Sample Test Case
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")