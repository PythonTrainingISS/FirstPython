s="python's"
print(s)
print('-'*13)
print(s.capitalize())
#String raw string,Byte string
file_path = r'C:\Python34'
print(file_path)
#bytes string
s=b'ravi'
print(s)
print(type(s))
s2=s.decode('ascii')#convert bytes to unicode
print(s2)
print(s2.encode("ascii"))#Unicode to byte code
