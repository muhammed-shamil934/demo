def sample():
    print("apple")
sample()
def add():
    a=2
    b=3
    print(a+b)
add()

def sum(x,y):
    z=x+y
    print(z)
sum(1,2)
sum(5,6)

def less(x,y):
    a=x-y
    print(a)
less(9,8)
def multi(x,y):
    b=x*y
    print(b)
multi(2,5)
def divid(x,y):
    c=x/y
    print(c)
divid(10,2)

def arbitrary(*x):
    print(x[3])
arbitrary("apple","orenge","lemon","banana")

def arbitrary(*x):
    print(x[3]+x[1])
arbitrary(1,5,8,6,8,7,10)

def keyword(a,b,c):
    print(b)
keyword(c=1,b=2,a=3)

def arbitrarykw(**a):
    print(a["x"])
arbitrarykw(x=1,y=2,z=3)

def defult(x=2):
    print(x)
defult(4)
defult()

def statment(x):
    return (x+10)
print(statment(5))

def passstat():
    pass

#arbitrary calculation 
