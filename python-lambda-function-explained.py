# What is a lambda function?
# It's a small, anonymous function you write in one line.

# Example: Add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Why use lambda? It's quick for simple tasks, like sorting.
numbers = [(2, 'b'), (1, 'a'), (3, 'c')]
# Sort by the first element
sorted_numbers = sorted(numbers, key=lambda item: item[0])
print(sorted_numbers)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# You can use lambda with map() to double numbers in a list
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6, 8]
