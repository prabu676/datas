day = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
print(day)
a = int(input("Enter your Number:"))

if a == 1:
    print(day[1])
elif a == 2:
    print(day[2])
elif a == 3:
    print(day[3])
elif a == 4:
    print(day[4])
elif a == 5:
    print(day[5])
elif a == 6:
    print(day[6])
elif a == 7:
    print(day[7])
else:
    print("Enter Valid Number")
