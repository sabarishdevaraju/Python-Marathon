x = 5
def set_x(num):
    x = num
    print(x)

def set_global_x(num):
    global x             # if global keyword is present, x = num change global values x = 5 -> 6
    print(x)
    x = num
    print(x)


print(x)
set_x(50)
x = 20
print(x)
set_global_x(6)
print(x)