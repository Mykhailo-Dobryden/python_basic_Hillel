"""4. Написати функцію, яка повертає поточний час. І обернути її у декоратор
  який відрахує 3 секунди.
  Приклад:
  what_time_is_it_now()
  3
  2
  1
  '16:21'
  Повернути час допоможе метод time.strftime з аргументом '%H:%M'"""
from datetime import datetime
import time


def sleep_for_3_seconds(func):
    def wrapper():
        print("what_time_is_it_now()")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func()
    return wrapper


@sleep_for_3_seconds
def what_time_is_it_now():
    time_now = datetime.now().strftime("%H:%M")
    return print(time_now)


what_time_is_it_now()

