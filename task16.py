# Ismi 5 harfdan uzun bo‘lgan talabalarni chiqaring.

with open("Input/students.txt", "r") as infile, \
     open("output/output16.txt", "w") as outfile:
       
    for line in infile:
        ism = line.strip()
        if len(ism) > 5:
            print(f"{ism} ismida {len(ism)} ta harf bor!")
            outfile.write(f"{ism} ismida {len(ism)} ta harf bor!\n")