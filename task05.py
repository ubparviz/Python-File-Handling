# Fayldagi sonlar o‘rtachasini (average) hisoblang.

numbers = []

with open("Input/numbers.txt", "r") as infile, \
     open("output/output05.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        numbers.append(number)
    
    average = sum(numbers)/len(numbers)
    print(average)
    outfile.write(str(average))