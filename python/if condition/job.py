age = int(input("Enter your Age:"))

if age>=18:
    exp = int(input("Enter your Experience(in numbers):"))
    if exp >0:
        print("Congrats!,Your are Eligible for Job")
    else:
        print("sorry!, We expect minimum 1 year of experience.Thank you for your Response")
else:
    print("Must be above 18")
        
