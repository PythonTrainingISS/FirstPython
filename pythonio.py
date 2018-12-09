"""demo for IO"""
try:
    name = input('enter  name:')
    city = input('enter city:')
    zip_code = int(input('enter the postal code:'))
    print('name:', name)
    print('city:', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as err:
    print(err)

print('next statement after try and except')
