import os

# path = os.path.normpath("C:\\Windows\\Web")
# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))
# print(os.path.islink(path))


# path = os.path.normpath("new_dir")
# os.mkdir(path)
# os.rmdir(path=path)

# file = open("file.txt", "w")
# file.write("Hello world!")
# file.close()
# file = open("file.txt", "a")
# file.write(" Hello user!")
# file.close()
# file = open("file.txt", "r")
# print(file.read())
# file.close()

# with open("file.txt", "w") as file:
#  file.write("Hello world!")
# with open("file.txt", "a") as file:
#  file.write(" Hello user!")
# with open("file.txt", "r") as file:
#  print(file.read())

import os
def file_collector(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files": []}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)

    with open("skiper.txt","w") as file:
        file.write("\n{:-^50}\n".format("Directories"))
        for dir in result["dirs"]:
            file.write(f"\t{dir}\n")
        file.write("\n{:-^50}\n".format("Files"))
        for files in result["files"]:
            file.write(f"\t{files}\n")

path =  "C:\\Windows\\Web"
file_collector(path)


for i in range(50,1,-1):
    print("{j:-^50}".format(name="*",j=str(i)))