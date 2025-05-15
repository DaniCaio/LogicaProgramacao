# 1. Faça um programa que implemente um menu onde o usurário deverá selecionar 1 ou 0. Caso seja entrado
# um número diferente, o programa deverá solicitar uma nova opção.

print ("Menu:")
print("Selecione uma opção:")
print("1 - Opção 1")
print("2 - Opção 2")

menu = int(input("Digite a opção desejada: "))

while menu != 1 and menu != 2:
    print("Numero invalido")
    menu = int(input("Digite a opção desejada: "))

print(f"Você escolheu a opção: {menu}")
