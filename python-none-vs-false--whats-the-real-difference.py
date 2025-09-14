# Define two variables
a = None
b = False

# Print their types
print("Type of a:", type(a))  # <class 'NoneType'>
print("Type of b:", type(b))  # <class 'bool'>

# Compare them directly
print("Is a equal to b?", a == b)  # False

# Check their truthiness
if a:
    print("a is truthy")
else:
    print("a is falsy")  # This will run

if b:
    print("b is truthy")
else:
    print("b is falsy")  # This will also run