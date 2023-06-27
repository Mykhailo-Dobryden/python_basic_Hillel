"""1. Напишіть програму, яка вітає користувача, виводячи слово `Hello`,
введене користувачем ім'я та розділові знаки за зразком: Hello, Kitty!"""

user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")

# or

print("Hello, {}!".format(user_name))

# or

print("Hello, %s!" % user_name)
