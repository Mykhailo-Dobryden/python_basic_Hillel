"""Довжина маршруту велоралі "100 кілометрів за 10 годин" - приблизно 100 кілометрів.
Велосипедист Вася стартує з нульового кілометра маршруту та їде зі швидкістю `v` кілометрів на годину.
На якій відмітці він зупиниться через `t` годин?
Програма отримує на вхід значення `v` та `t`. Якщо `v > 0`, то Вася рухається
у позитивному напрямку за маршрутом, якщо ж значення `v < 0`, то негативному.
Програма має вивести ціле число від 0 до 100 – номер позначки, на якій зупиниться Вася."""

speed = int(input("Enter a speed of cyclist: "))
hours = int(input("Enter a duration of movement: "))

mark_number = 0

if speed > 0:
    mark_number = speed * hours
if speed < 0:
    mark_number = abs(speed * hours)

print(f"{mark_number} - it is a number of mark where cyclist Vasya will stop")
