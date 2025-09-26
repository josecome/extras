# Create an empty list to store 
# the square values
squares = []

# Loop through numbers from 0 to 4
for i in range(5):
    # Append the square of each 
    # number to the list
    squares.append(i**2)

# Use list comprehension to generate 
# a list of squares from 0 to 4
squares = [i**2 for i in range(5)]

# Use list comprehension to generate 
# squares of even numbers from 0 to 9
squares = [
    i**2 for i in range(10)
    # Include only even numbers
    if i % 2 == 0
    ]
print(squares)