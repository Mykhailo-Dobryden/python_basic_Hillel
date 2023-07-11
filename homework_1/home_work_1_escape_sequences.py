from tabulate import tabulate

print("Таблиця escape-послідовностей:")
sequences = [
    ["\\a", "Bell (alert)"],
    ["\\b", "Backspace"],
    ["\\n", "New line"],
    ["\\t", "Horizontal tab"],
    ["\\", "Backslash"],
    ["\"", "\"Double quotation mark\""],
    ["\'", "\'Single quotation mark\'"],
    ["\\r", "Carriage Return"],
    ["\\f", "Formfeed"],
    ["\\v", "Vertical Tab"],
    ["\\0", "Null Character"],
    ["\\N{Name}", "Unicode character Database named lookup"],
    ["\\uxxxxxxxx", "Unicode character with a 16-bit hex value"],
    ["\\Uxxxxxxxx", "Unicode character with a 32-bit hex value"],
    ["\\000", "Character with octal value ooo"],
    ["\\xhh", "Character with hex value hh"],
]

headers = ["Symbols", "Definition"]

print(tabulate(sequences, headers, tablefmt="outline"))
