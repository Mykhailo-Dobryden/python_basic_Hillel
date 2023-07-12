"""* Написати функцію яка прибере з dict елементи із значеннями None:
{'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
Повинно повернути {'first_color': 'Red', 'second_color': 'Green'} #
* dict може бути довільним"""


def rm_none_item(data: dict):
    """Return a dict without items with values 'None'"""
    new_dict = {k: v for k, v in data.items() if data.get(k) is not None}
    return new_dict


my_dict = {'first_color': None,
           'second_color': 'Green',
           'second_co': '',
           'third_color': None,
           'name': 'kolya',
           'position': None,
           'salary': 10000,
           'believer': True,
           }

print(rm_none_item(my_dict))
