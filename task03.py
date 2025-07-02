# Fayldagi eng katta sonni aniqlang.

numbers = []

with open("Input/numbers.txt", "r") as infile, \
     open("output/output03.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        numbers.append(number)
    
    max = max(numbers)
    print(max)
    outfile.write(str(max))