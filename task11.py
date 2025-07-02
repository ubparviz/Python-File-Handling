# students.txt Fayldagi barcha ismlarni ekranga chiqaring.

with open("Input/students.txt", "r") as infile, \
     open("output/output11.txt", "w") as outfile:
       
    intext = infile.read()
    print(intext)
    outfile.write(intext)