import  sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5)
print(sys.getrecursionlimit())

def fact(n):
    if n:
        return n*fact(n-1)
    else:
        return 1

print(fact(3))