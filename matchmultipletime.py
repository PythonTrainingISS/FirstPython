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
pattern='P+?N'
for m in re.finditer(pattern,s,re.I):
    print(m.group())
    print(m.span())
    print()

print(re.findall(pattern,s,re.I))