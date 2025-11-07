# Print the reverse of a number using arithmetic only
num = int(input("Enter a number to reverse: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse of number:", rev)
