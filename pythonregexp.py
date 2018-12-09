import re

s='root:x:0:0:root:/root:/bin/bash'

pattern=':'
replacement=','

s2 = re.sub(pattern,replacement,s)
print(s2)
print()

s3= re.sub('[AEIOU]','*',s2,flags=re.I)
print(s3)

s3= re.sub('[AEIOU]','*',s2,flags=re.I,count=3)
print(s3)

items = re.split('[,:/;]',s)
print(items)

items = [item for item in enumerate(re.split('[,:;/]',s)) if item[1]]
print(items)

