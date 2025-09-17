# Word frequency using dictionary comprehension

sentence = "Python is fun and Python is good"
words = sentence.lower().split()

word_freq = {
    word: words.count(word) 
    for word in set(words)
    }

print(word_freq)