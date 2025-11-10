tu = ("deva","sachin","aathi","Rajesh")
print("Before tuple:",tu)
li = (list(tu))

li.sort()
tup=tuple(li)

print("After sorted tuple:",tup)

print(type(tup))