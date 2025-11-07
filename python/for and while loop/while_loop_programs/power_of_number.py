base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1
i = 0

while i < exp:
    result *= base
    i += 1

print("Result:", result)
