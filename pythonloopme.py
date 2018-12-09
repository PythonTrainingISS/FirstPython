items=[2.2,'pam',1.2,'kim',3,4.5,.98,'pat']
print(items)

items[-5] = 'kimberly'#update
print(items)

items.append('stat')
print(items)
items.insert(0,'mumbai')
print(items)
value=items.pop()
print('item popped',value)

#delete by value remove only removes first occurence
items.remove('pam')
print(items)

item1=[1.1,1.2,1.3,1.5,1.6]
print(item1*2)
print(item1)
temp=['alpha','beta','charlie']
print(enumerate(temp))
for index,value in enumerate(temp):
    items.insert(index,value)

print(items)

for index,value in enumerate('peter'):
    print(index,value)

duplicates = [2.2,1.3,4.4,4.5,2.2]
print(set(duplicates))



#multidimensional list
mat=[[1,2,3],[6,5,4],[7,8,9]]
mat[1][1]='X'
print(mat)

mat[2].append(10)
print(mat)

mat.insert(1,['a','b','c'])
print(mat)

for row in mat:
    for col in row:
        print(col,end='\t')
    print()

names=['pam','allen','tim','neil','joe']
names.sort()
print(names)

def by_secondname(name):
    return name[1]

names.sort(key=by_secondname)
print(names)

#lambda function
"""syntax:
lambda arg1,arg2,arg3,......:expression
"""
names.sort(key=lambda  name:name[1])
print(names)

"""Dictionary"""

info={'host':'wsl','domain':'rootcap.in','desc':'web server','app':'apache httpd','version':2.2}
item='versoin'
if item in info:
    info[item]=3.7
print(info)

info.pop('desc')
print(info)

print(info.get('app'))

#Iteration of dictionary
for key,value in info.items():
     print(key,':',value)

#github.com/ravijaya/datafiles