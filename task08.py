# Fayldagi sonlar ichidan 5 ga karralilarni sanang va ularni chiqaring.

with open("Input/numbers.txt", "r") as infile, \
     open("output/output08.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        if number % 5 == 0:
            print(number)
            outfile.write(f"{number}\n")