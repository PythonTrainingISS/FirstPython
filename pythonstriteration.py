#Spring Iteration

s  = "this is a simple String in python"
for temp in s:
    if temp not in 'aeiou':
        print(temp,':',ord(temp))
    else:
        print('*'*4)
    