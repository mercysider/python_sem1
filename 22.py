s1 = int(input("Введите размер первого списка: "))
s2 = int(input("Введите размер второго списка: "))
list_1 = [int(input(f"Введите {i+1} элемент первого списка: ")) for i in range(s1)]
list_2 = [int(input(f"Введите {i+1} элемент второго списка: ")) for i in range(s2)]
print(sorted(set(list_1).union(set(list_2))))