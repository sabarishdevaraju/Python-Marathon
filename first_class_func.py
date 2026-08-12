def create_adder(x):
    def adder(y):
        return x+y
    def subtractor(y):
        return x-y
    return adder, subtractor

add_40, sub_40 = create_adder(40)  #A function instance with x=40 is created and saved
#print(add_40(100))
#print(add_40(120))
#print(add_40(1000))
#print(add_40(1120))
#print(sub_40(100))
#print(sub_40(120))
#print(sub_40(1000))
#print(sub_40(1120))

l = [100,120,1000,1120]
for v in l:
    print(add_40(v))
    print(sub_40(v))

print(list(map(lambda y:y+40, l)))
print(list(map(sub_40, l)))    # map(func, *iterables)

print(list(filter((lambda x: x >= 1000), l)))

"""
first class functions:
add_40, sub_40 = create_adder(40)      #  Create_adder()  → creates a create_adder instance/object with x = 40
                         │
                         ▼
                 ┌───────────────────┐
                 │ create_adder(40)  │
                 │                   │
                 │ x = 40            │
                 └─────────┬─────────┘
                           │
                 creates two functions
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       ┌─────────────┐           ┌──────────────┐
       │ adder(y)    │           │ subtractor(y)│
       │             │           │              │
       │ return x+y  │           │ return x-y   │
       └─────────────┘           └──────────────┘
              │                         │
              └────────────┬────────────┘
                           ▼
              return adder, subtractor
                           │
                           ▼
              (adder, subtractor)
                    tuple returned
                           │
                           ▼
             tuple unpacking happens
                    /             \
                   /               \
                  ▼                 ▼
              add_40              sub_40
                 │                   │
                 ▼                   ▼
          refers to adder      refers to subtractor


"""


