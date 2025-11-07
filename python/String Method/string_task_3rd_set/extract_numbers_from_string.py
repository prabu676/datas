text = "abc123xyz"
numbers = ""
for ch in text:
    if ch.isdigit():
        numbers += ch
print(numbers)
