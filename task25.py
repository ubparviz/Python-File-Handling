# OutPut25 fayliga faqat 5 baho olganlarni yozing.

with open("Input/grades.csv", "r") as infile, \
     open("output/output25.txt", "w") as outfile:
    
    lines = infile.readlines()

    outfile.write("Bahosi 5 bo'lgan o'quvchilar:\n")
    print("Bahosi 5 bo'lgan o'quvchilar:")

    for line in lines[1:]:
        name, grade = line.strip().split(",")
        grade = int(grade)

        if grade == 5:
            result = f"{name} — {grade}"
            print(result)
            outfile.write(result + "\n")

