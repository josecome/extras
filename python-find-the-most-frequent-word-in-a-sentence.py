# Find the most common word in a sentence 
# using dictionary comprehension
sentence = "Python is fun and Python is good"
words = sentence.lower().split()

# Count word frequency
freq = {
    word: words.count(word) 
    for word in set(words)
    }

# Find the most common word
most_common = max(freq, key=freq.get)

print("Most common word:", most_common)