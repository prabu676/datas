print("Checking Given number is Positive & Even")

a = int(input("Enter the Number:"))

if a>0:
    if a%2 == 0:
        print(a, "is a Positive Number & Even Number")
    else:
        print(a, "is a Positive Number But not a Even Number ")
else:
    print(a,"is not a Positive number, Please Enter Positive number")
