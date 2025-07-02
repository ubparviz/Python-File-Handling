# Barcha baholarning o‘rtachasini hisoblang.

total_grade = 0
total_students = 0

with open("Input/grades.csv", "r") as infile, \
     open("output/output20.txt", "w") as outfile:
    lines = infile.readlines()

    for line in lines[1:]:
        name, grade = line.strip().split(",")
        grade = int(grade)

        result = f"O'quvchi: {name}, Baho: {grade}"
        print(result)
        outfile.write(f"{result}\n")

        total_grade += grade
        total_students += 1

    average = total_grade / total_students
    print(f"O'rtacha baholar: {average}")
    outfile.write(f"O'rtacha baholar: {average}")