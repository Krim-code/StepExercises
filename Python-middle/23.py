import os

os.chdir("C:\\Users\\Redmi\\Desktop\\New folder\\")
print(os.getcwd())
for i in range(100):
    os.mkdir(f"{i}")
    os.chdir(f"C:\\Users\\Redmi\\Desktop\\New folder\\{i}")
    a = open(f"test.txt","w")
    a.write("Hello, world!")
    os.chdir("C:\\Users\\Redmi\\Desktop\\New folder\\")
