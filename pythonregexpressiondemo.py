"""
regex:
    operations:
            pattern match
            find and replace
            split

    default chars:
            case sensitive
            match only once in aline
            substring
            greedy in nature
"""

import re

s= 'the python and the perl scripting'
#pattern = 'P.+N'#Greedy match
pattern = 'P.+?N'#NonGreedy match
m=re.search(pattern,s,re.I)
if m:
    print('match string',m.group())
    print(m.start())
    print(m.end())
    before=s[:m.start()]
    after=s[m.end():]
    print('before:',before)
    print('after:',after)
else:
    print('Failed to match')
print(m)