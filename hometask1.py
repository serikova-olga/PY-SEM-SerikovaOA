# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

a=int(input('input digit '))
if a==1 or a==2 or a==3 or a==4 or a==5:
    print ('week day')
elif a==6 or a==7:
    print ('day off')
else:
    print ('not a day of week')


