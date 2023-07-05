"""2. Користувач вводить число `X`, яке має два знаки після десяткової точки.
  - Виведіть його дрібну частину.
  - Виведіть першу цифру після десяткової точки."""

number_x = input("Enter a number that has 2 characters after the decimal point:  ").strip()

number_x_parsed = number_x.split('.')
fractional_part = number_x_parsed[1]

print(f"Fractional part of {number_x} is: {fractional_part[:2]}")
print(f"First digit of {number_x} after the decimal point is: {fractional_part[:1]}")
