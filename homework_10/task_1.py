"""
1. Програма яка при запуску повинна:
Створити текстовий файл, записати в нього дані, які вводить користувач.
Закінченням введення нехай служить порожній текст. Кожен введений текст у файлі повинен
починатися з нового рядка. Також треба спитати назву файлу у користувача.
"""


def user_inputs() -> list:
    """Returns a list with strings. User can enter text until he enters an empty string ''. """
    list_with_text = []
    while True:
        entered_text = input("Enter a txt: ")
        list_with_text.append(entered_text)
        if entered_text == '':
            break
    return list_with_text


def ask_file_name():
    """Returns name for .txt file """
    file_name = input("Enter name for file: ")
    return f"{file_name}.txt"


def write_to_file(file_name: str, data: list):
    """Writes an iterable data to the file"""
    with open(f"{file_name}", 'w') as f:
        for i in data:
            f.writelines(f"{i}\n")


def main():
    # text_to_write = user_inputs()  # Ask user to enter a text
    # name_for_file = ask_file_name()  # Ask a name for file
    # write_to_file(name_for_file, text_to_write)  # Create file and write date there
    write_to_file(ask_file_name(), user_inputs())


if __name__ == '__main__':
    main()




