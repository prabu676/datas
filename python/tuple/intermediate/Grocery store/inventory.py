inventory = [
["Fruits", ["Apple", "Banana", "Mango"]],
["Vegetables", ["Carrot", "Tomato", "Spinach"]],
["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
print("************Task-1************")
for item in inventory:
    category,items = item
    print(f" Category: {category}")
    for thing in items:
        print(f"- {thing} ")
    print()

print("************Task-2************")

inventory[0][1].append("orange")
print(inventory)

print("************Task-3************")

inventory[1][1].remove("Spinach")
print(inventory)

print("************Task-4************")

for category in inventory:
    print(f"{category[0]}: {len(category[1])} items")

print("************Task-5************")

for item in inventory:
    category,items = item
    print(f" Category: {category}")
    for thing in items:
        print(f"- {thing} ")
    print()