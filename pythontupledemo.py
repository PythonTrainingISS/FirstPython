t=(1.1,'pam',3,4,5)
print(t)
print(type(t))
print(len(t))
print(t[-1])
print(t[:-1])
print()
for item in t:
    print(item)

n=(1000,)
print(n)
print(type(n))

s='peter',
print(s)

"""
Application of tuple:
parallel assignment
"""
name,age,gender=t='sarah',3,'female'
print(name,age,gender)

divmod(8,5)
print(divmod(8,5))

q,r = divmod(8,5)
print(q)
print(r)

def sqt_n_cube(value):
    return value**2,value**3

print(sqt_n_cube(2))

#set intersection

items1=[1,2,3,4,5]
item2=[1,3,5,7,9]
x=set(items1)
y=set(item2)
print(x.intersection(y))
print(x.difference(y))
print(x-y)
print(y-x)
print(list(x.intersection(y)))
print(x|y)

items=[2,1,3,4,4,3,5,7,9,7,6]
temp=list()

for item in items:
    temp.append(hex(item))

print(temp)

temp2 =[i if i%2 == 0 else bin(i) for i in items]
print(temp2)

lines = [line for line in open('password.txt') if line.startswith('a')]
print(lines)

temp={item for item in items}
print(temp)
print()
print(type(temp))

