# Numbers between 1 and 100 divisible by 6 but not by 9
for i in range(1, 101):
    if i % 6 == 0 and i % 9 != 0:
        print(i, end=" ")
