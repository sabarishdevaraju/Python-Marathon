file_name = input("Enter the file name or path to read: ")
f = open(file_name, "r")
print(f.read())
f.close()