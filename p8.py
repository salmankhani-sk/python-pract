def reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
print(reverse("hello world"))