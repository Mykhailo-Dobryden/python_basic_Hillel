"""У математиці функцію `sign(x)` (знак числа) визначено так:
sign(x) = 1, якщо x > 0,
sign(x) = -1, якщо x < 0,
sign(x) = 0 якщо x = 0.
Для цього числа x виведіть значення sign(x).
Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else."""

x = int(input("Enter number for x in function sign(x): "))

sign_x = int

if x > 0:
    sign_x = 1
elif x < 0:
    sign_x = -1
else:
    sign_x = 0

print(sign_x)

