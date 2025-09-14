my_dict = {"name": "Jose"}

# Safe access using .get()
print(my_dict.get("age"))  # Output: None

# Risky access using brackets
# print(my_dict["age"])	# KeyError: 'age'

# Output: Not provided
print(my_dict.get("age", "Not provided"))  