"""2. Написати калькулятор температури.
    Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт,
    Кельвін відповідно) Програма має вивести температуру у трьох шкалах
    температур – Цельсій, Фарренгейт, Кельвін."""


def user_input_temp() -> tuple:
    """Return a tuple of two values: 1st - temperature, 2nd - the type of scale"""
    t = float(input("Enter a temperature: "))
    t_scale = (input("Choose a temperature scale (Celsius - C;"
                     " Kelvin - K; Fahrenheit - F): ")).upper()

    # Verification of entered values for appropriate temperature scale:
    if t_scale == 'C' and t < -273.15:  # for Celsius scale
        raise ValueError("Minimum allowed temperature for Celsius is -273.15. "
                         "Please, enter a correct value")
    if t_scale == 'K' and t < 0:  # for Kelvin scale
        raise ValueError("Minimum allowed temperature for Kelvin is 0. "
                         "Please, enter a correct value")
    if t_scale == 'F' and t < -459.67:  # for Fahrenheit scale
        raise ValueError("Minimum allowed temperature for Fahrenheit degrees is -459.67. "
                         "Please, enter a correct value")
    else:
        return t, t_scale


def converter_temperatures(data) -> tuple:
    """Return a tuple of converted temperatures: c - Celsius; k - Kelvin, f - Fahrenheit"""
    temperature = data[0]
    scale = data[1]
    c = 0  # Celsius
    k = 0  # Kelvin
    f = 0  # Fahrenheit

    # Here we convert Celsius degrees to Kelvin and Fahrenheit degrees:
    if scale == 'C':
        c = temperature
        k = temperature + 273.15
        f = round(temperature * 9 / 5 + 32, 2)

    # Here we convert Kelvin degrees to Celsius and Fahrenheit degrees:
    if scale == 'K':
        c = round(temperature - 273.15, 2)
        k = temperature
        f = round(temperature * 9 / 5 - 459.67, 2)

    # Here we convert Fahrenheit degrees to Celsius and Kelvin degrees:
    if scale == 'F':
        c = round((temperature - 32) * 5 / 9, 2)
        k = round((temperature - 32) * 5 / 9 + 273.15, 2)
        f = temperature

    return c, k, f


try:
    user_data = user_input_temp()
    result = converter_temperatures(user_data)
    celsius, kelvin, fahrenheit = result
    print(f"Celsius: {celsius} °C\n"
          f"Kelvin: {kelvin}K \n"
          f"Fahrenheit: {fahrenheit} °F")
except ValueError as e:
    print(e)

