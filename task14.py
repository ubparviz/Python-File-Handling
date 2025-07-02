# Ismlarni teskari tartibda chiqaring.

with open("Input/students.txt", "r") as infile:
    names = infile.readlines()
    
with open("Output/output14.txt", "w") as outfile:
    for name in reversed(names):
        print(name)
        outfile.write(name)
