# Count how many numbers between 1 and 200 are divisible by both 4 and 6
count = 0
for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0:
        count += 1
print("Count of numbers divisible by 4 and 6:", count)
