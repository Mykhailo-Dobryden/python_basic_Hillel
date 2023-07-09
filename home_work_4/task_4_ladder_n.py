"""4. По даному натуральному `n ≤ 9` виведіть драбинку з `n` сходинок,
`i`-я сходинка складається з чисел від 1 до `i` без прогалин.
  1
  12
  123
  1234
  12345
  """

# ------------first variant


def get_num_ladder(num: int):
    if 0 < num <= 9:
        v = ''
        for i in range(1, num + 1):
            v += str(i)
            print(v)
    else:
        print("Enter a number in range between 1 and 9")


# ---------second variant


def get_stairs(num):
    if 0 < num <= 9:
        for i in range(1, num+1):
            for j in range(1, i+1):
                print(j, end='')
            print()
    else:
        print("Enter a number from 1 to 9")


user_num = int(input("Enter a number: "))

print("First variant: ")
get_num_ladder(user_num)
print("Second variant: ")
get_stairs(user_num)