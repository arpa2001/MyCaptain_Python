import math

a0 = int(input("Enter the first term:      "))
a1 = int(input("Enter second term:         "))
n = int(input("Enter the number of terms: "))

a2 = a0 + a1
print("Series:\n\t",a0,"\n\t",a1)
for i in range(n-2):
    a2 = a0 + a1
    print("\t",a2)
    a0 = a1
    a1 = a2