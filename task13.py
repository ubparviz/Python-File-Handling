# Ismlarni alfavit bo‘yicha tartiblang.

students = open("Input/students.txt","r+")

names = students.readlines()

result = sorted(names)
print(result)

students2 = open("Output/output13.txt","w")
students2.writelines(result)