#5. Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
from math import sqrt


x1=float(input ('input x1 '))
y1=float(input ('input y1 '))
x2=float(input ('input x2 '))
y2=float(input ('input y2 '))
a=sqrt((x1-x2)**2 + (y1-y2)**2)
print (a)