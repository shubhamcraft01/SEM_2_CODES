# 1. Read the first line of input (array of integers separated by space)
# and convert it into a list of integers
try:
    arr = list(map(int, input().split()))

    # 2. Read the last line of input (the key element to be searched)
    key = int(input())

    # 3. Perform Linear Search
    # We use range(len(arr)) to keep track of the index
    found = False
    for i in range(len(arr)):
        if arr[i] == key:
            print(i)
            found = True
            break  # Exit loop once the first occurrence is found

    # 4. If the loop finishes and the element was never found
    if not found:
        print("Not found")

except EOFError:
    pass