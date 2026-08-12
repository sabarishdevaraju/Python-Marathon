l = ['apple','orange','banana'] # LIST FOR LOOP 
for v in l:
    print("I am eating {} -> listaddress: {} -> stringaddress : {}".format(v,id(l),id(v)))



print("------------------------------\n")


s = {1,2,3,4,'string',2.34} # set for loop

for a in s:
    print("#{} -> set address : {} -> address : {}".format(a,id(s),id(a)))


print("------------------------------\n")

print(list(range(0,100)))


print("------------------------------\n")

for i in range(25, 100):
    print(i)
    if i >= 43:
       break # break will exit for loop 

print("------------------------------\n")

for i in range(1,50):
    if i % 2 == 0:
        continue # continue will skip even numbers
        print(f"This is printed only for even numbers-->{i}")
    else:
        print(f"This is printed only for odd numbers-->{i}")

print("Loop exited")