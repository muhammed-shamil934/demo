a=[10,20,30,40,50,]
print(a)
print(type(a))
print(len(a))
print(20 not in a)
for i in a:
    print(i)
print(a[1:])
print(a[1:5])
print(a[:6])
print(a[-3:-6])
a[1]=12
print(a)
a.append(60)
print(a)
a.insert(3,44)
print(a)
b=[5,6,7,8,9,]
a.extend(b)
print(a)
a.remove(5)
print(a)
a.pop(4)
print(a)
a.pop()
print(a)
del a[5]
print(a)
c=["oreng","apple","banana","mango"]
print(c)
c.sort()
print(c)
e=c.copy()
print(e)
y=list(a)
print(y)
d=c+a
print(d)
print(a.count(10))
a.clear()
print(a)
del a
print(a)