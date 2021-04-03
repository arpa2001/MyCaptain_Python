list1 = list(input("Input: list1 = "))
print("Output: "),
for i1 in list1:
    if int(i1) >= 0:
        print(i1),

print("\n")

list2 = list(input("Input: list2 = "))
result = []
print("Output: "),
for i2 in list2:
    if int(i2) >= 0:
        result.append(i2)
print(result)