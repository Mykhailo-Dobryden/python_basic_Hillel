"""2. Користувач вводить число `X`, яке має два знаки після десяткової точки.
  - Виведіть його дрібну частину.
  - Виведіть першу цифру після десяткової точки."""
import math

number_x = float(input(
    "Enter a number that has 2 characters after the decimal point:  ").strip())

two_digit_part = int(round(number_x - math.floor(number_x), 2) * 100)
one_digit_part = int(round(number_x - math.floor(number_x), 2) * 10)

print(
    f"Fractional part of {number_x} is: {two_digit_part}")
print(
    f"First digit of {number_x} after the decimal point is: {one_digit_part}")



