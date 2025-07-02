# Ismi “A” harfi bilan boshlanuvchilarni alohida ro‘yxatga oling (a_names.txt).

A_names = []

with open("Input/students.txt", "r") as infile, \
     open("output/output17.txt", "w") as outfile:
       
    for line in infile:
        ism = line.strip()
        
        if ism[0].lower() == "a":
            print(f"{ism}")
            A_names.append(ism)
            outfile.write(f"{ism}\n")
    
    print(A_names)