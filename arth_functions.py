def basic_math(x,y,k, l=20):  # default l = 20
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    return {
        "Addition" : a,
        "Subtraction": s,
        "Division": d,
        "Multiplication": m
    }

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

d = basic_math(k = 6, y = a, x = b, l ) # y = a Keyword Arguments          """ 6,l Positional arguments followed by Keyword arguments"""

print(f"Basic Math Results of {a} and {b}")

k = d.keys()
v = d.values()
print(k)
print(v)
for i in d:
    print(f"{i} : {d[i]}")