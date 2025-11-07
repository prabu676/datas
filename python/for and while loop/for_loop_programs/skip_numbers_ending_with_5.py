# Print numbers from 1 to 100 but skip numbers ending with digit 5
for i in range(1, 101):
    if i % 10 == 5:
        continue
    print(i, end=" ")
