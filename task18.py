# Foydalanuvchi ism kiritadi, u faylda mavjudmi — shuni tekshiradigan dastur yozing.

Names = []

with open("Input/students.txt", "r") as infile, \
     open("output/output18.txt", "w") as outfile:
       
    for line in infile:
        ism = line.strip().title()
        print(f"{ism}")
        Names.append(ism)
        
    your_name = input("Ismingizni kiriting: ").strip().title()

    if your_name in Names:
        print("Ismingiz mavjud")
    else:
        print("Ismingiz mavjud emas")