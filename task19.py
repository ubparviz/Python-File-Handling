# Barcha o‘quvchilar ismi va bahosini ekranga chiqaruvchi dastur yozing.

with open("Input/grades.csv", "r") as infile, \
     open("output/output19.txt", "w") as outfile:
    
    lines = infile.readlines()

    for line in lines[1:]:
        name, grade = line.strip().split(",")
    
        result = f"O'quvchi: {name}, Baho: {grade}"
        print(result)
        outfile.write(f"{result}\n")
