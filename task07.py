# Fayldagi har bir sonni kvadratga ko‘paytirib ekranga chiqaring.

with open("Input/numbers.txt", "r") as infile, \
     open("output/output07.txt", "w") as outfile:
    
    for line in infile:
        number = int(line.strip())
        kvadrati = pow(number, 2)

        print(kvadrati)
        outfile.write(f"{kvadrati}\n")