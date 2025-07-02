# Bahosi 5 bo‘lganlar sonini hisoblang.

total_5grade = 0

with open("Input/grades.csv", "r") as infile:
    lines = infile.readlines()


for line in lines[1:]:
    name, grade = line.strip().split(",")
    grade = int(grade)

    if grade == 5:
        total_5grade += 1

print(f"Bahosi 5 bo'lganlar soni {total_5grade}")

with open("output/output22.txt", "w") as outfile:
    outfile.write(f"Bahosi 5 bo'lganlar soni {total_5grade}")