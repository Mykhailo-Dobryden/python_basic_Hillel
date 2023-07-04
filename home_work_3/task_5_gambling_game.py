"""5. Користувач вводить число від 1 до 10,
програма генерує рандомне число від 1 до 10,
якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'.
Дати користувачеві три спроби;)"""

import random

attempt = 0
while attempt < 3:
    user_number = int(input("Enter your number in range between 1 and 10: "))
    cpu_number = random.randint(1, 10)
    print(f"CPU choice: {cpu_number}")
    if user_number == cpu_number:
        print("You won!")
        break
    else:
        print(f"You lose! The number of chances: {2 - attempt}!")
        attempt += 1



