print("Check Student Qualify for Work:")

mark = int(input("Enter your Mark:"))

if mark>=175:
    att = input("Enter your Attenance Percentage:")
    if att >="60%":
        print("Congrats!,you're Eligible for the Scholarship")
    else:
        print("You're not Eliguble,Percentage Must be above 60%")
else:
    print("Must be mark above 175")
    
