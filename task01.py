# Fayldagi barcha sonlarni ekranga chiqaruvchi dastur yozing.

with open("Input/numbers.txt", "r") as infile, \
     open("output/output01.txt", "w") as outfile:
       
    intext = infile.read()
    print(intext)
    outfile.write(intext)