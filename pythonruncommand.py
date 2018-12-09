import subprocess
import  sys
if  sys.platform=='linux':
    cmd=['ipconfig']
else:
    cmd=['ipconfig']

op=subprocess.check_output(cmd )
print(op)
print(op.decode('ascii'))

#indexing
s='perl'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
#print(s[4])

s1='perl'
print(s1[len(s1)-1])

#slicing name[start-index"ex-of-end-index]

s2 = 'perlandpython'
print(s2[0:4])
print(s2[4:7])
print(s2[-6:])
print(s2[:])
print(s2[1:-1])
print(s2[-6:-4])

#Iteration
ord('A')