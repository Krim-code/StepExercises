d = {
    "name": "Кирилл",
    "login": "simple kiril",
    "password": "1234"
}

def output(person):
    print("{:*^50}".format("Информация о пользователе"))
    print(f"\tname -\t{person['name']}")
    print(f"\tlogin -\t{person['login']}")
    print(f"\tpassword - \t{person['password']}")
output(d)
