# Factorial of a given number
n = int(input("Enter number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)
