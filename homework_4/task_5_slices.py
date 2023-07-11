"""5. Дано рядок.
  a. Виведіть третій символ цього рядка.
  b. виведіть передостанній символ цього рядка.
  с. виведіть перші п'ять символів цього рядка.
  d. виведіть весь рядок, крім двох останніх символів.
  e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
        тому символи виводяться починаючиз першого).
  f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
  g. виведіть усі символи у зворотному порядку.
  h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
  i. виведіть довжину цього рядка."""

row = input("Enter something long: ")

print(f"a) Third symbol: {row[2]}")
print(f"b) The last but one symbol: {row[-2]}")
print(f"c) The first 5 symbols: {row[:5]}")
print(f"d) The whole row without last 2 symbols: {row[:-2]}")
print(f"e) Only symbols with even index: {row[::2]}")
print(f"f) Only symbols with odd index: {row[1::2]}")
print(f"g) Symbols in reverse order: {row[::-1]}")
print(f"h) Each second symbols in reverse order: {row[::-2]}")
print(f"i) The length of the row: {len(row)}")
