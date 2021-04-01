import math
import os
import mimetypes

# Calculating Radius
r = float(input("Input the radius of the circle: "))
pi = math.pi
area = pi*(r*r)
print(f"The area of the circle with radius {r} is:\n{area}")

print("\n")

# Finding Extension
mimetypes.init()
fnm = input("Input the Filename: ")
nm, extnsn = os.path.splitext(fnm)
etyp = mimetypes.types_map[extnsn]
print(f"The extension of the file is: '{etyp}'")
