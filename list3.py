a=[1,2,3,4,5,6,7,8]
print(a)
print(type(a))
print(len(a))
print(5 not in a)
for i in a:
    print(i)
print(a[1:])
print(a[1:5])
print(a[:6])
print(a[-3:-6])
a[3]=99
a.append(88)
print(a)
a.insert(2,67)
print(a)
b=[44,55,66,77,88,]
a.extend(b)
print(a)
a.remove(3)
print(a)
a.pop(1)
print(a)
del a[1]
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
print(a.count(88))
a.clear()
print(a)
del a
print(a)