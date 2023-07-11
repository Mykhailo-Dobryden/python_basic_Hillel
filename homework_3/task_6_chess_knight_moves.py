"""6. Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі
в будь-якому напрямку і на одну клітинку по горизонталі, чи навпаки.
Дані дві різні клітини шахівниці, визначте, чи може кінь потрапити з
першої клітини на другу одним ходом. [Опціонально]"""

chess_map = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
}

start_position = input("Enter start position: ").lower().strip()
end_position = input("Enter start position: ").lower().strip()

start_col = chess_map[start_position[0]]
end_col = chess_map[end_position[0]]
start_row = int(start_position[1])
end_row = int(end_position[1])


if abs(end_col - start_col) == 2 and abs(end_row - start_row) == 1 or \
        abs(end_col - start_col) == 1 and abs(end_row - start_row) == 2:
    print("The move of the knight is possible")
else:
    print("The move of the knight is not possible")
