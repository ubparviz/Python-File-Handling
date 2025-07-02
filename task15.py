# students.txt faylidagi har bir ism nechta harfdan iboratligini ko‘rsating.


with open("Input/students.txt", "r") as infile, \
     open("output/output15.txt", "w") as outfile:
       
    for line in infile:
        ism = line.strip()
        print(f"{ism} ismida {len(ism)} ta harf bor!")
        outfile.write(f"{ism} ismida {len(ism)} ta harf bor!\n")