towar = []


def append_towar(towar):
    num_towar = int(input("Введите количество товаров"))
    for i in range(num_towar):
        el = input("Введите название товара")
        towar.append(el.lower())
        print(towar)


def check_towar(towar):
    check = input("Введите товар:")
    if check.lower() in towar:
        print("Товар есть")
    else:
        print("Tовара нет")


append_towar(towar)
check_towar(towar)
