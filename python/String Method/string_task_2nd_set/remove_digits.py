text = "Python123 is easy 456"
result = ""
for ch in text:
    if not ch.isdigit():
        result += ch
print("String after removing digits:", result)
