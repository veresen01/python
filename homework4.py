#Вычислить число c заданной точностью d
# n=float(input('введите число'))
# d=float(input('введите точность'))
# if d==1:
#     print(int(n))
# else:
#     d=str(d)
#     d=d.split(".")
#     d=len(d[1])
#     print(round(n,d))

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
# n=int(input('введите число'))
# a=[]
# for i in range(2, n+1):
#     if n % i==0:
#         for j in range(2, i//2+1):
#             if i%j==0:
#                 break
#         else:
#             a.append(i)
# print(a)

#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# a= [2,5,8,8,3,0,3,2]
# b=[]
# for i in a:
#     if a.count(i)==1:
#         b.append(i)
# print(b)


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')
