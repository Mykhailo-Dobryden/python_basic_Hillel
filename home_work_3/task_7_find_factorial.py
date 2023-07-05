"""7. Написати програму, яка знайде факторіал введеного користувачем числа.
Наприклад, факторіал числа 5 дорівнює добутку 1*2*3*4*5 = 120.
Формула знаходження факторіалу:
n! = 1 * 2 * ... * n, де n - введене користувачем число."""

number = int(input("Enter number: "))
n_fctr = 1

if number < 0:
    print("Entered number should be a positive integer")
else:
    for i in range(1, number + 1):
        n_fctr *= i
        i += 1

print(f"{number}! = {n_fctr}")
