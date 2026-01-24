print("\nTry This 4: String Processing")
print("=" * 50)

# Sample text data
text = "  Python is a powerful programming language. It's used for data science, web development, and automation.  "
print(f"Original text: '{text}'")

# Basic string cleaning
# .strip() removes leading/trailing whitespace; .lower() standardizes casing
cleaned = text.strip().lower()
print(f"Cleaned: '{cleaned}'")

# Word analysis
# Cleaning punctuation before splitting into a list
words = cleaned.replace(",", "").replace(".", "").replace("'", "").split()
print(f"Words: {words}")

# Word frequency
word_freq = {}
for word in words:
    # .get(word, 0) handles new words by starting the count at 0
    word_freq[word] = word_freq.get(word, 0) + 1

print(f"Word frequency: {word_freq}")

# Most common words
# Sorting the dictionary by value (count) in descending order
most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Most common words: {most_common}")

# String formatting examples
name = "Alice"
age = 25
languages = ["Python", "JavaScript", "SQL"]

print(f"\nString formatting examples:")
print(f"f-string: {name} is {age} years old and knows {', '.join(languages)}")
print("format(): {} is {} years old and knows {}".format(
    name, age, ', '.join(languages)))

# Text transformation
sentences = text.strip().split('.')
# Re-assembling sentences with proper capitalization
capitalized_sentences = [s.strip().capitalize() +
                         '.' for s in sentences if s.strip()]
print(f"Capitalized sentences: {capitalized_sentences}")
