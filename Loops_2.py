def positivecal(listx):
    listy = []
    buff = ""
    for i in listx:
        if i == "[":
            continue
        if i == "]":
            listy.append(int(buff))
        if i == "," or i == " ":
            listy.append(int(buff))
            buff = ""
            continue
        buff += i
    result = []
    for j in listy:
        if int(j) >= 0:
            result.append(int(j))
    return result


list1 = list(input("Input: list1 = "))
print("Output: ", end="")
for n in positivecal(list1):
    if n != positivecal(list1)[0]:
        print(",", end=" ")
    print(n, end="")

print("\n")

list2 = list(input("Input: list2 = "))
print(f"Output: {positivecal(list2)}")