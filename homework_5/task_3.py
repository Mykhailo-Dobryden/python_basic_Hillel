"""3. Написати функцію яка поверне площу фігури: за замовчуванням трикутника,
опціонально квадрату. На вході 2 величини та параметр типу фігури."""


def get_area_of_figure(h, w, figure='triangle') -> float:
    """Return the area of figure. By default, it will be area for triangle,
    in case if figure=='square', return area for square"""
    area = 0.5 * h * w
    if figure == 'square':
        area = h * w
    return area


def get_user_request():
    """Return a tuple with next values: (height, width, figure)"""
    figure = input("For which geometric figure to calculate area? (triangle/square): ")
    height = float(input("Enter a height of the figure: "))
    width = float(input("Enter a width of figure: "))
    return height, width, figure


parameters_of_figures = get_user_request()
user_height, user_width, user_figure = parameters_of_figures
area_of_figure = get_area_of_figure(user_height, user_width, figure=user_figure)
print(f"The area of {user_figure} is {area_of_figure}")
