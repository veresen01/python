#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# n = int(input('введите кол-во элементов'))
# some_list=[]
# summ=0
# for _ in range(n):
#     num=int(input('введите элемент списка'))
#     some_list.append(num)
#
# for index in range(1,n,2):
#     summ+=some_list[index]
# print(summ)

#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# n = int(input('введите кол-во элементов'))
# some_list=[]
# for _ in range(n):
#     num=int(input('введите элемент списка'))
#     some_list.append(num)
# new_list=[]
# for index in range((n-1)//2+1):
#     num1=some_list[index]
#     num2 = some_list[n-index-1]
#     new_list.append(num1*num2)
# print(new_list)

#Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# n = int(input('введите кол-во элементов'))
# some_list=[]
# for _ in range(n):
#     num=input()
#     some_list.append(num)
# minn=1
# maxx=0
# for el in some_list:
#     if '.' in str(el):
#         dr=str(el).split('.')[1]
#         if float('0.'+dr)>maxx:
#             maxx=float('0.'+dr)
#         elif float('0.'+dr) < minn:
#             minn = float('0.' + dr)
# print(maxx-minn)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# a = int(input('введите число'))
# b = ' '
# while a!=0:
#     b=str(a%2)+b
#     a//=2
# print(b)
