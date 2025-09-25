# Create a list of fruits
fruits = ['apple', 'banana', 'cherry']

# Loop through the list using the index
for i in range(len(fruits)):
    # Print the index and the fruit at that index
    print(i, fruits[i])

# Loop through the list using enumerate to get both index and value
for i, fruit in enumerate(fruits):
    # Print the index and the fruit
    print(i, fruit)

# Loop through the list using enumerate, starting the index from 1 instead of 0
for i, fruit in enumerate(fruits, start=1):
    # Print the index and the fruit in a formatted string
    print(f'{i}. {fruit}')