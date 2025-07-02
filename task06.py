# Fayldagi barcha toq sonlarni output06.txt fayliga yozing.

numbers = []

with open("Input/numbers.txt", "r") as infile, \
     open("output/output06.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        if number % 2 != 0:
            numbers.append(number)
    
    print(numbers)
    outfile.write(str(numbers))