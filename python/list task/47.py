nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = []
for sub in nested:
    for i in sub:
        flat.append(i)
print(flat)
