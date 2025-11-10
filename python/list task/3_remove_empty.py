a = ["a","b","","c",""]
print("Before",a)
b=[]
for i in a:
    if i!= "":
        b.append(i)
print("after",b)
