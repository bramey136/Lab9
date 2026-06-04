def get_word_counts():
    text = """Mr. Bennet replied that he had not. But it is, returned she; 
    for Mrs. Long has just been here, and she told me all about it."""

    words = text.lower().split()

    cleaned_words = []
    for word in words:
        word = word.strip(".,!?;:\"'")
        cleaned_words.append(word)

    word_counts = {}
    for word in cleaned_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_top_10_frequent_words():
    word_counts = get_word_counts()
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for i, (word, count) in enumerate(sorted_words[:10], start=1):
        print(f"{i}. {word}: {count}")


print_top_10_frequent_words()

"""
This program counts word frequencies and prints the top 10 most common words.
"""