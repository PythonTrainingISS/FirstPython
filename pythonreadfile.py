import csv
fp=open('password.txt')
for temp in fp:
    #print(temp,end='')
    print(temp.split(':',-1))
    filecontent=temp.split(':',-1)
print(fp)
print('-------------now---------------------------------')

count =dict()
for row in csv.reader(open('password.txt'),delimiter=':'):
    print(row[-1])
    shell= row[-1]
    count[shell]=count.get(shell,0)+1
print('-------------now---------------------------------')
print(count)

#find frequency of last occurence


fp.close()
