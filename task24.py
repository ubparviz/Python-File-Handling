# O‘rtacha bahodan yuqori olganlar ro‘yxatini chiqaring.
total_grade = 0
total_students = 0
students = []

with open("Input/grades.csv", "r") as infile, \
     open("output/output24.txt", "w") as outfile:
    lines = infile.readlines()

    for line in lines[1:]:
        name, grade = line.strip().split(",")
        grade = int(grade)

        students.append((name, grade))

        result = f"O'quvchi: {name}, Baho: {grade}"
        print(result)
        outfile.write(f"{result}\n")

        total_grade += grade
        total_students += 1

    average = total_grade / total_students
    avg_text = f"O'rtacha baholar: {average:.2f}"
    print(avg_text)
    outfile.write(avg_text + "\n")

    outfile.write("\nO'rtacha bahodan yuqori olganlar:\n")
    print("\nO'rtacha bahodan yuqori olganlar:")
    for name, grade in students:
        if grade > average:
            line = f"{name} - {grade}"
            print(line)
            outfile.write(line + "\n")
