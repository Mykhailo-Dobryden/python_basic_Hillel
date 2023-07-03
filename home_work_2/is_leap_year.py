"""Дано натуральне число. Потрібно визначити, чи є рік із цим числом високосним.
Якщо рік є високосним, то виведіть `YES`, інакше виведіть `NO`.
Нагадаємо, що відповідно до григоріанського календаря, рік є високосним,
якщо його номер кратний 4, але не кратний 100, а також якщо він кратний 400."""

leap_year = int(input("Enter a year: "))

if leap_year % 400 == 0 or (leap_year % 4 == 0 and leap_year % 100 > 0):
    print("Yes")
else:
    print("No")

