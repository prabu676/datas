num = int(input("Enter a number: "))
sum_sq = 0

while num > 0:
    digit = num % 10
    sum_sq += digit ** 2
    num //= 10

print("Sum of squares of digits:", sum_sq)
