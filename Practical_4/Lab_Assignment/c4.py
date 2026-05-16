import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# 1. Group products by Date
grouped = df.groupby('Date')['Product'].apply(list)

# 2. Find all pairs of products sold together per date
pair_counts = Counter()

for products in grouped:
    # combinations ensures we get unique pairs. 
    # Sorting ensures (A, B) and (B, A) are treated as the same pair.
    if len(products) > 1:
        pairs = combinations(sorted(products), 2)
        pair_counts.update(pairs)

# 3. Find the maximum frequency
if pair_counts:
    max_freq = max(pair_counts.values())

    # 4. Filter all pairs that have the maximum frequency
    most_frequent_pairs = [pair for pair, count in pair_counts.items() if count == max_freq]

    # 5. Output the result in the exact format shown in the test case
    # Note: the test case sorts results alphabetically by product name
    most_frequent_pairs.sort()
    
    for pair in most_frequent_pairs:
        print(f"{pair[0]} and {pair[1]}: {max_freq} times")