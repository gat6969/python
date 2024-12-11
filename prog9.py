
with open("sample.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")


with open("sample.txt", "r") as file:
    contents = file.read()


print("Contents of the file:")
print(contents)
