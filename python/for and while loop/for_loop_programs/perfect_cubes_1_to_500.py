# Count how many numbers between 1 and 500 are perfect cubes
count_cubes = 0
for i in range(1, 501):
    if round(i ** (1/3)) ** 3 == i:
        count_cubes += 1
print("Perfect cubes between 1 and 500:", count_cubes)
