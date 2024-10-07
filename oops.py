class sample:
    x=10
y=sample()
print(y.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("shamil",21)
print(p1.name,p1.age)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def new(self):
        print(self.name,self.age)

class student(person):
    pass
v=student("shamil",21)
v.new()

a=[1,2,3,5,6,]
print(len(a))
b={9,7,6,5,4}
print(len(b))
c=(0,9,8,7)
print(len(c))
d={"name":"shami","place":"malappuram","age":21}
print(len(d))
f="apple,orenge"
print(len(f))