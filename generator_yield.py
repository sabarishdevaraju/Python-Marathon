def double_numbers(iterable):
    for i in iterable:
        print(f"[] double data gen {i}")
        yield i*2   # yield give value at every loop  to the function

x = double_numbers(range(1000))
for i in x:
    print(i)

print("---------------------------------------\n")

def datagen():
    l = []
    for i in range(10):
        print(f"[] data gen {i}")
        l.append(i)
    return l  # return give value once loop is completes to the function



for i in datagen():
    print(i)

print("----------------------------------\n")

def numbers():       # generator function
    yield 10         # yield keyword
    yield 20
    yield 30

g = numbers()        # generator object

print(next(g))              # asks generator for next value
print(next(g)) 
print(next(g)) 
print(g)


"""
 
Call double_numbers(range(3))
          │
          ▼
   Generator created
          │
      for asks next
          ▼
       i = 0
          │
      yield 0
          │
          ├────► for gets 0
          │
       PAUSE ⏸️
          │
      for asks next
          │
       RESUME ▶️
          │
       i = 1
          │
      yield 2
          │
          ├────► for gets 2
          │
       PAUSE ⏸️
          │
      for asks next
          │
       RESUME ▶️
          │
       i = 2
          │
      yield 4
          │
          ├────► for gets 4
          │
       PAUSE ⏸️
          │
      for asks next
          │
       RESUME ▶️
          │
   for loop finished
          │
          ▼
 Generator CLOSED ✅



"""