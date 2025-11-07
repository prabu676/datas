# Sum of all odd numbers from 1 to 50
sum_odd = 0
for i in range(1, 51):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers from 1 to 50:", sum_odd)
