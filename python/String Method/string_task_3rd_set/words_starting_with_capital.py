text = "This is a Test Sentence With Some Words."
words = text.split()
for word in words:
    if word[0].isupper():
        print(word)
