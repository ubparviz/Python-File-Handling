# Sonlar ro‘yxatini tartiblab, output10.txt fayliga yozing.

numbers = []

with open("Input/numbers.txt", "r") as infile, \
     open("output/output10.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        numbers.append(number)
    
    numbers = sorted(numbers)
    print(numbers)
    outfile.write(str(numbers))