# Read the 11 player heights from one line of input
try:
    heights = list(map(int, input().split()))
    
    # Use max() to identify the tallest player
    if heights:
        print(max(heights))
except EOFError:
    pass