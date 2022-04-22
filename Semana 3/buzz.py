numero = int(input("Digite um número inteiro: "))
div = numero % 5 == 0

while numero:
    print("\t" + str(numero))
    numero = numero+1
