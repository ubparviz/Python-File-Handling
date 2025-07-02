# Fayldagi sonlar yig‘indisini hisoblang.

total = 0

with open("Input/numbers.txt", "r") as infile, \
     open("output/output02.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        total += number
        
    print(total)
    outfile.write(str(total))