#3. Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
x=int(input ('input x '))
y=int(input ('input y '))
if x>0 and y>0:
    print ('first quater')
elif x>0 and y<0:
    print ('second quater')
elif x<0 and y<0:
    print ('third quater')
elif x<0 and y>0:
    print ('forth quater')
else:
    print ('not a quater')