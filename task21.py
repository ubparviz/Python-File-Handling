# Eng yuqori baho olgan o‘quvchini toping.

students = []
total_grade = 0

with open("Input/grades.csv", "r") as infile:
    lines = infile.readlines()


for line in lines[1:]:
    name, grade = line.strip().split(",")
    students.append({"name": name, "grade": grade})



with open("output/output21.txt", "w") as outfile:
    top_grade = max(s['grade'] for s in students)
    top_students = [s['name'] for s in students if s['grade'] == top_grade]

    top_result = f"Eng yuqori baho: {top_grade} — {', '.join(top_students)}"
    print(top_result)
    outfile.write(top_result + "\n")
