# Fayldagi barcha juft sonlarni chiqaring.

numbers = []

with open("Input/numbers.txt", "r") as infile, \
     open("output/output04.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        if number % 2 == 0:
            numbers.append(number)
    
    print(numbers)
    outfile.write(str(numbers))