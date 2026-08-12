

def keywordargs(**kwargs):
    print(kwargs)
    return kwargs


keywordargs(a=1,b=2,c=3,d=4,e=5,f=6)


print("----------------------------------\n")


def keyword_args(x,y,l=120,*z,**kwargs):  # arguments cannot follow var-keyword argument
     print(kwargs)
     print(x)
     print(y)
     print(l)
     print(z)
     return kwargs

keyword_args(1,2,3,4,5,6,7,8,9,a=1,b=2,c=3,d=4,e=5,f=6)

print("----------------------------------\n")

def keyword_args(x,z,*y): 
     print(x)
     print(y)
     print(z)

keyword_args(1,2,3,4,5,6,7,8,9)