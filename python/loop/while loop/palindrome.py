num = int(input("Enter the number:"))
temp =num
rev =0
while temp >0:
    digit = temp%10
    print(digit)
    rev = rev*10+digit
    print(rev)
    temp //=10

if num == rev:
    print("palindrome number")
else:
    print("Not a palindrome number")
