import string
text = "Hello, world! Python is great."
for ch in string.punctuation:
    text = text.replace(ch, "")
print(text)
