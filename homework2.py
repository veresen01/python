#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# number = input('Введите число: ')
# summ=0
# for symbol in number:
#     if symbol !='.' and symbol !='-':
#         summ+=int(symbol)
# print(summ)


#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# N = int(input('Введите N: '))
# some_list=[1]
# fact=1
# for i in range(2, N+1):
#     fact*=i
#     some_list.append(fact)
# print(some_list)

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# n = int(input('Введите N: '))
# summ=0
# for i in range(1,n+1):
#     summ+=(1+1/i)**i
# print(summ)