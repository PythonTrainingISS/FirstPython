import  re
from fileinput import filelineno,filename,input
def demo():
    print('null arguments')


print(demo)#will return memory address
print(type (demo))

def demo(a,b):
    print(a+b)

def power(x,n):
    """power raises x to n
    defaullt argument should be given right to left
    """
    return x**n

print(pow(2,3))

"""
variable length argument
"""

def demovarlen(*args):
    print(args)

demovarlen()
demovarlen(1)
demovarlen(1,2,3,'iii')

items=[11,12,13]
demovarlen(items)

items=(11,12,13)
demovarlen(items)
demovarlen(*items)

"""
"""

def compute(a,b,c):
    print(a+b+c)

items = [11,22,33]
compute(*items)
compute(items[0],items[1],items[2])

items = [11,22,33,44]
compute(*items[1:4])
compute(items[0],items[1],items[2])

def grep_me(pattern,*args):
    for line in input(args):
        if re.search(pattern,line,re.I):
             print('{}:{}:{}'.format(filename(),filelineno(),line),end='')

grep_me('root','password.txt','password.dat')

name,age='sarah',3
print('I am {},{} years old'.format(name,age))

"""keyword argument parameter"""

def tuner(**kwargs):
    print(kwargs)
print('--'*10)
tuner();
tuner(contrast=0.8,brightness=0.79,hue=0.85)
param = dict(contrast=0.8,brightness=0.79,hue=0.85)
tuner(**param)# passing a dict content as argument to key

def demo(value):
    value.pop()
    value.remove(1)

n=[1,2,3,4]
demo(n)
print(n)
#print('prinrt')
#n=set(1,2,3,4)
#demo(n)
print('print')
print(n)

"""scoope for function and variable"""
print('----------------------------scoope for function and variable----------------------------------------------------------')
n=10

def demoscope():
    print(n)

demoscope()
print(n)


