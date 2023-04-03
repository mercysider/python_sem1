# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите число элементов массива: "))
array = list()

for i in range(N):
    num = int(input(f"Введите элемент {i+1} массива: "))
    array.append(num)

X = int(input("Введите искомое число: "))

min = abs(array[0] - X)
closer_num = array[0]

for i in range (1,N):
    if abs(array[i] - X) < min:
        min = abs(array[i] - X)
        closer_num = array[i]

print(f"Максимально близкое к {X} число в массиве {array}: {closer_num}")