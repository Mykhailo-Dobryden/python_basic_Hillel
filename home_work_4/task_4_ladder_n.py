"""4. По даному натуральному `n ≤ 9` виведіть драбинку з `n` сходинок,
`i`-я сходинка складається з чисел від 1 до `i` без прогалин.
  1
  12
  123
  1234
  12345
  """


def get_num_ladder(num: int):
    if 0 < num <= 9:
        v = ''
        for i in range(1, num + 1):
            v += str(i)
            print(v)
    else:
        print("Enter a number in range between 1 and 9")


user_num = int(input("Enter a number: "))

get_num_ladder(user_num)
