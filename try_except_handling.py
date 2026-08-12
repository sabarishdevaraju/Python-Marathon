try:
    c = a + b
except:
    print("some happenend message")

print("------------------------\n")

import sys
a = 10
#b = [1,2,3,4]
c = 2

try:
    c = a + b[c]
    print("Value of c is {}".format(c))
except NameError as e:
    print("Name error happened")
    print(e)
except IndexError as e:
    print("Index error happened")
    print(e)
else:
    print("All good")
finally:
    print("whatever the case is, I will work") # it always run at the end (eg:cleanup work)


print("------------------------\n")

import sys
a = 10
b = [1,2,3,4]
c = 5

try:
    c = a + b[c]
    print("Value of c is {}".format(c))
except NameError as e:   # object refered to e 
    print("Name error happened")
    print(e)
except IndexError as e:
    print("Index error happened")
    print(e)
else:
    print("All good")
finally:
    print("whatever the case is, I will work") # it always run at the end (eg:cleanup work)

print("------------------------\n")

a = 10
b = [1,2,3,4]
c = 2

try:
    c = a + b[c]
    raise IOError("This is a sample error")
    print("Value of c is {}".format(c))
except NameError as e:   # object refered to e 
    print(f"Name error happened: {e}")
except IndexError as e:
    print(f"Index error happened: {e}")
except Exception as e:
    print(f"something else: {e}")
    print(f"Error: {sys.exc_info()[0]}")
else:
    print("All good")
finally:
    print("whatever the case is, I will work") # it always run at the end (eg:cleanup work)

print("------------------------\n")

def divide(a,b):
    if b == 0:
        raise Exception("Cannot divide by zero")
    return a/b

try:
    c = divide(5, 0)
    raise IOError("This is a sample error")
    print("Value of c is {}".format(c))
except NameError as e:   # object refered to e 
    print(f"Name error happened: {e}")
except IndexError as e:
    print(f"Index error happened: {e}")
except Exception as e:
    print(f"something else: {e}")
    print(f"Error: {sys.exc_info()}")
else:
    print("All good")
finally:
    print("whatever the case is, I will work") # it always run at the end (eg:cleanup work)


print("------------------------\n")

import sys
a = 10
b = [1,2,3,4]
c=  2

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

try:
    c = divide(5, b[2])
    print("Value of c is {}".format(c))
except (NameError, IndexError, KeyError) as e:   # object refered to e 
    print(f"Error happened: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
else:
    print("All good")
finally:
    print("whatever the case is, I will work") # it always run at the end (eg:cleanup work)
