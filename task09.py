# Sonlar nechta raqamdan iboratligini (1 xonali, 2 xonali...) aniqlang.

with open("Input/numbers.txt", "r") as infile, \
     open("output/output09.txt", "w") as outfile:
    
    for line in infile:
        number = line.strip()
        print(f"{number} soni {len(number)} xonali")
        outfile.write(f"{number} soni {len(number)} xonali\n")