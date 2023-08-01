"""1. Написати функцію, яка рахуватиме кількість очок футбольної команди.
Перемога дає 3 очки, нічия 1 очко, поразка -1 очко.
Функція приймає три аргументи – win, draw, loss.
Приклад : count_points(3, 2, 2) -> 9"""


def count_points(win, draw, loss):
    """Function takes 3 arguments, where:
    1st arg - wins; 2nd arg - draws; 3rd arg - losses. Returns a total points"""
    return win * 3 + draw * 1 + loss * (-1)


print(count_points(5, 2, 0))

