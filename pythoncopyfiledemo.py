with open ('password.txt')  as fp,open('password.dat','w') as fw:
    """context manager: programming constructor of python
    to do IO"""
    fw.write(fp.read())