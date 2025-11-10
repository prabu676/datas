abc = (4,5,6,7,4,8,4,9,7,9)
print("Tuple with duplicate values:",abc)

duplicate_values= []

for i in abc:
    if abc.count(i) > 1 and i not in duplicate_values:
        duplicate_values.append(i)

print("Duplicate Values are:",duplicate_values) 


