# Create a list of numbers
nums = [1, 2, 3, 4, 5]

# Method 1: Using a regular for 
# loop to square each number
squared = []
for n in nums:
    squared.append(n ** 2)
print("Regular:", squared)

# Method 2: Using list comprehension 
# to achieve the same result
squared_comp = [n ** 2 for n in nums]
print("Comprehension:", squared_comp)

