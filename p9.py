def reverse_words(word):
    words = word.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverse_words('Python is fun'))