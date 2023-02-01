""""
a program script that prints
the first 2 letters
the last 2 letters
the middle word(s)
from the string: "Enzo Fernandez"
"""

name ="Enzo Fernandez"
print("first 2:",name[0:2])
print("last 2:", name[-2:])
mid =len(name)//2
print ("middle element:", name[mid:mid+2])