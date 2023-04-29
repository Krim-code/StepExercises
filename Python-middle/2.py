import os.path


def file_collection(path):
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    for path, dirname, filename in os.walk(path):
        for dir in dirname:
            result["dirs"].append(dir)
        for file in filename:
            result["files"].append(file)
    print(result)

    with open("skan.txt","w") as file:
        file.write("\n{:-^50}\n".format("Directory"))
        for dir in result["dirs"]:
            file.write(f"\t\t{dir}\n")
        file.write("\n{:-^50}\n".format("Files"))
        for f in result["files"]:
            file.write(f"\t\t{f}\n")




file_collection("C:\\Windows\\Web")
