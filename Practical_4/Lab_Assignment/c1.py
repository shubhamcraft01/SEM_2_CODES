import pandas as pd

# 1. Prompt for the file name
file_name = input()

# 2. Load the data
df = pd.read_csv(file_name)

# 3. Preprocessing: Convert 'Date' to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# 4. Calculate total sales for each row
df['Sales'] = df['Quantity'] * df['Price']

# 5. Extract Month and Year for grouping (format: YYYY-MM)
df['Month'] = df['Date'].dt.to_period('M')

# 6. Group by Month and sum the sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# 7. Find the month with the highest total sales
# idxmax() returns the index (month), while max() returns the value
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

# 8. Output results formatted as per test case
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")