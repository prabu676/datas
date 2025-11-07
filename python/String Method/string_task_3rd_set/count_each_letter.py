text = "Hello World"
text = text.replace(" ", "").lower()
letters = {}
for ch in text:
    letters[ch] = letters.get(ch, 0) + 1
for k, v in letters.items():
    print(k, ":", v)
