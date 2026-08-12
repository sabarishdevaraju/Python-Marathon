def add(x,y):
    z = x + y
    print(f"Result is {z}")
    return z

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(f"Addition of {a} and {b} is {add(a,b)}")