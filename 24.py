n = int(input("Введите кол-во кустов: "))
bushes = list()

for i in range(n):
    bush = int(input(f"Ягод на {i+1} кусте: "))
    bushes.append(bush)

max = 0
posit = -1

for i in range(len(bushes)):
    if bushes[i-2] + bushes[i-1] + bushes[i] > max:
        max = bushes[i-2] + bushes[i-1] + bushes[i]
        if i == 0:
            posit = n
        else:
            posit = i

print(f"Максимум ягод за раз: {max} можно собрать, если машина подъедет к {posit} кусту")
      