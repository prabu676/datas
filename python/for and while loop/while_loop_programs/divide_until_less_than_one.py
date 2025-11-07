num = float(input("Enter a number: "))
count = 0

while num >= 1:
    num /= 2
    count += 1

print("Number of divisions:", count)
