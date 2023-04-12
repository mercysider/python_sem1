def pow(a, b):
    if b == 1:
        return a
    return(a*pow(a, b-1))

a = int(input("Число A: "))
b = int(input("Число B: "))
print(pow(a,b))