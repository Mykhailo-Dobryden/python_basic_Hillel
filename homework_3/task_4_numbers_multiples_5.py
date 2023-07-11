"""Даний список:
list_of_six = [100, 106, 112, 118, 124, 130, 136,
142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

Надрукувати всі числа, які діляться на 5 без залишку, але не більше 150."""

# --------------First variant------------------

list_of_six = list(range(100, 197, 6))

for num in list_of_six:
    if (num % 5) == 0 and num < 150:
        print(num)


# --------------Second variant------------------

list_of_six = list(range(100, 197, 6))
multiples_5 = [i for i in list_of_six if i % 5 == 0 and i < 150]
print(f"Second variant: {multiples_5}")
