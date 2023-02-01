"""
A program script that prints:
3 times a srting stored in the variable str,
followed by its first 9 characters
"""

name = "indomitable"
print(name*3)
for k  in range(9):
    print(name[k],end="")
