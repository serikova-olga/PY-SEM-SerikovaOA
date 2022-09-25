#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
n=int(input ('input quater number '))
if n==1:
    print ('range is x>0 and y>0')
elif n==2:
    print ('range is x>0 and y<0')
elif n==3:
    print ('range is x<0 and y<0')
elif n==4:
    print ('range is x<0 and y>0')
else:
    print ('not a quater')