from unicodedata import decimal


a=float(input('write a number'))
a=int(a*10%10)
if a!=0:
    print(a)
else:
    print('no')