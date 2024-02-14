num = []
for i in range(10):
    value = float(input(f"Enter value {i + 1}: "))
    num.append(value)


largest = num[0]


for x in num:
    if x > largest:
        largest = x


print(f"The largest number in the list is: {largest}")
