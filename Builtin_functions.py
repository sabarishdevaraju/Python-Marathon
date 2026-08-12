l = ['apple','kiwi','orange','dragon']

print(type(enumerate(l)))

e = enumerate(l)
print(list(enumerate(l, start=1)))  # enumerate() builtin functions
for i in range(len(l)):
  print(e.__next__())