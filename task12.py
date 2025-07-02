# Ismlar sonini hisoblang.

ismlar = []

with open("Input/students.txt", "r") as infile, \
     open("output/output12.txt", "w") as outfile:
       
    for line in infile:
        ism = line.strip()
        print(ism)
        outfile.write(f"{ism}\n")
        ismlar.append(ism)
    
    print(f"\nIsmlar soni {len(ismlar)} ta")
    outfile.write(f"\nIsmlar soni {len(ismlar)} ta")