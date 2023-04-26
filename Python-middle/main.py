import os

# print(os.name)
# print(os.getcwd())
#
# os.chdir("C:\\")
# print(os.getcwd())
# os.mkdir("It works")
# os.mkdir(os.path.join(path,"1"))

path = os.path.normpath("C:\\Users\\Redmi\\Desktop\\dir\\1")
os.chdir(path)
print(os.getcwd())
with open("Text.txt", "r") as file:
    # file.write("Привет ,что то там ,но это работает")
    a = file.read()
    print(a)