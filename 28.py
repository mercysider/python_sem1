def sum(a, b):
    if a == 1 and b == 1:
        return a+b 
    if a > 1:
        return sum(a-1,b) + 1
    if b > 1:
        return sum(a,b-1) + 1

a = int(input("Число A: "))
b = int(input("Число B: "))
print(sum(a,b))