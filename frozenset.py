a=[1,2,3,4,5,]
a[1]=20
print(a)
b=frozenset(a)
print(b)
"""b[3]=70
print(b)"""


#errors
try:
    print(x)
except:
    print("an error is there")
else:
    print("no error in there")
finally:
    print("program complited")
try:
    print(x)
except NameError:
    print("x is not difain")
except:
    print("an error in there")
y=int(input("enter a number"))
if y<0:
    raise Exception("number <0 is not allowed")