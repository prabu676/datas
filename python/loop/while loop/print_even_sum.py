num =int(input("Enter the number:"))
summ=0


while num>0:
    digit = num%10

    if digit%2 ==0:
        summ +=digit


    num//=10

print(summ)
