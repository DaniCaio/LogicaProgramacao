# # 1. Imprimindo Números:
# for i in range(1, 11):
#     print(i)

# # 2. Imprimindo Números Ímpares:
# for i in range (1, 10, 2):
#     print(i)

# 3. Imprimindo Números em Intervalo Personalizado: -----verificar e pegar certinho!!!!!!!---------

# numero1= int(input("Digite um número:" ))
# numero2= int(input("Digite um número:" ))

# if numero1 > numero2:
#     numero1, numero2 = numero2, numero1
#     print(f"numeros impares entre {numero1} e {numero2}:")

# for numero in range(numero1, numero2 + 1):
#     if numero % 2 != 0:
#         print(numero)

# 4. Tabuada:
# Escreva um programa que gere a tabuada de multiplicação de um número fornecido pelo usuário.

for i in range (1,11):
    mult= num * i
    print(f"{num} * {i} = {mult}")