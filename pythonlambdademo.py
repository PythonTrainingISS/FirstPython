""""
lambda funtions
syntax:
lambda arg1,,arg2.......:expression
"""
import re
power =lambda x,n=0:x**n

print(power)
print(power(3))
print(power(3,2))

items = [1,2,1,3,2,4,5]
m= map(hex,items)

print(m)

for item in m:
    print(item)

m= map(ord,'peter pan')
print(list(m))

values=[112, 101, 116, 101, 114, 32, 112, 97, 110]
"""
<ascii char="p">112</ascii>
"""

def tag_it(av):
    return '<ascii char={}>{}</ascii>'.format(chr(av),av)

m= map(tag_it,values)
print(m)
m=map(lambda av:'<ascii char={}>{}</ascii>'.format(chr(av),av),values)
for tag in m:
    print(tag)


# using custom filter

pattern = 'bash$'
def my_filter(func,seq):
    return [item for item in seq if func(item)]

f=my_filter(lambda line:re.search(pattern,line,re.I),open('password.txt'))

for matched_line in f:
    print(matched_line,end='')



