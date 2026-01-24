import string

print("\nLab Problem 2: Text Processing Engine")
print("=" * 50)

# Sample document
document = """
Python is a high-level programming language. Python was created by Guido van Rossum.
Python is widely used for web development, data science, and automation.
Python has a simple syntax that makes it easy to learn.
Many companies use Python for their backend systems.
Python's extensive library ecosystem makes it very powerful.
"""


def clean_text(text):
    """Clean and normalize text for analysis."""
    # Remove punctuation and convert to lowercase
    cleaned = text.lower()
    for punct in string.punctuation:
        cleaned = cleaned.replace(punct, ' ')
    return cleaned


def analyze_text(text):
    """Comprehensive text analysis."""
    cleaned = clean_text(text)
    # Filter out empty strings using 'if word'
    words = [word for word in cleaned.split() if word]

    # Basic statistics
    word_count = len(words)
    unique_words = len(set(words))
    avg_word_length = sum(len(word)
                          for word in words) / len(words) if words else 0

    # Word frequency mapping
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sorting by frequency (value)
    most_common = sorted(
        word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    # Sorting by string length (len)
    longest_words = sorted(set(words), key=len, reverse=True)[:5]

    # Mapping distribution of word lengths
    length_dist = {}
    for word in words:
        length = len(word)
        length_dist[length] = length_dist.get(length, 0) + 1

    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "avg_word_length": avg_word_length,
        "most_common": most_common,
        "longest_words": longest_words,
        "length_distribution": length_dist
    }


# Execute the analysis
analysis = analyze_text(document)

print("Text Analysis Report")
print("-" * 30)
print(f"Total words: {analysis['word_count']}")
print(f"Unique words: {analysis['unique_words']}")
print(f"Average word length: {analysis['avg_word_length']:.1f} characters")

print(f"\nMost common words:")
for word, count in analysis['most_common']:
    print(f"  {word}: {count}")

print(f"\nLongest words:")
for word in analysis['longest_words']:
    print(f"  {word} ({len(word)} characters)")

print(f"\nWord length distribution:")
for length, count in sorted(analysis['length_distribution'].items()):
    print(f"  {length} characters: {count} words")

# Advanced analysis: Sentence parsing
sentences = [s.strip() for s in document.split('.') if s.strip()]
sentence_lengths = [len(s.split()) for s in sentences]

print(f"\nSentence analysis:")
print(f"Number of sentences: {len(sentences)}")
if sentences:
    print(
        f"Average sentence length: {sum(sentence_lengths) / len(sentence_lengths):.1f} words")
    print(f"Shortest sentence: {min(sentence_lengths)} words")
    print(f"Longest sentence: {max(sentence_lengths)} words")
