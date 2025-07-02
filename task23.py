# Har bir baho nechi marta qatnashganini sanang (Counter dan foydalaning).

grade_counts = {}

with open("Input/grades.csv", "r") as infile:
    lines = infile.readlines()

for line in lines[1:]:
    name, grade = line.strip().split(",")
    grade = int(grade)

    if grade in grade_counts:
        grade_counts[grade] += 1
    else:
        grade_counts[grade] = 1

with open("output/output23.txt", "w") as outfile:
    for grade in sorted(grade_counts):
        outfile.write(f"{grade} baho {grade_counts[grade]} marta qatnashgan.\n")
        print(f"{grade} baho {grade_counts[grade]} marta qatnashgan.")