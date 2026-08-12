
import re

print("----------Heap update script-----------")

file_name = input("Enter the filename/companyname :")
with open(file_name, "r") as f:
   data = f.read()

new_memory = input("Enter the new Jobinram value:")
new_heap = input("Enter the new memory/maxmemory value:")

# Replace values
data = re.sub(r"^jobinram=.*", f"jobinram={new_memory}", data, flags=re.MULTILINE)
data = re.sub(r"^memory=.*", f"memory={new_heap}", data, flags=re.MULTILINE)
data = re.sub(r"^max-memory=.*", f"max-memory={new_heap}", data, flags=re.MULTILINE)

with open(file_name, "w") as f:
    f.write(data)

with open(file_name, "r") as f:
   print(f.read())

print("Configuration updated successfully!")
