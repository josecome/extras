# Define a list of names
names = ["Jose", "Jaime", "Come"]

# Define a corresponding list of scores
scores = [85, 92, 78]

# Loop through both lists at the same time 
# using zip()
# For each pair, print the name and their 
# score
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Combine the two lists into a list of 
# tuples using zip()
# Each tuple contains a name and the 
# corresponding score
combined = list(zip(names, scores))
print(combined)

# Convert the zipped result into a dictionary
# Each name becomes a key, and each score 
# becomes the value
data_dict = dict(zip(names, scores))
print(data_dict)
