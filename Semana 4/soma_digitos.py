#programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
ultimoDigito = 0
soma = 0
numero = int(input("Digite um número inteiro: "))

while numero != 0:
    ultimoDigito = numero % 10
    numero = numero // 10
    soma = soma + ultimoDigito
print(soma)
