from math import sqrt

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4*a*c
delta1 = sqrt(delta)
x1 = (-b + delta1)/2*a
x2 = (-b - delta1)/2*a

if x1 and x2 == 0:
    print("esta equação não possui raízes reais")
elif x1 and x2 ==
