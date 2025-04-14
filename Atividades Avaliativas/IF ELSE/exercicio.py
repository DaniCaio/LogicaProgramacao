# Exercício 1: Verificador de Números Pares e Ímpares

# numero = int(input("Digite um numero: "))

# if numero % 2 == 0:
#     print("O número é par")
# else: print("O número é ímpar")


# Exercício 2 : Maior número

# Descrição: Faça um programa que recebe dois números e imprime qual o maior.
# caso sejam iguais mostre uma mensagem "São iguais"

# numero1= int (input('Digite um número: '))
# numero2= int (input('Digite um número: '))

# if numero1 > numero2:
#     print(f"O número {numero1} é o maior")

# elif numero2 > numero1:
#     print(f"O número {numero2} é o maior")

# else:
#     print("Números são iguais")
    
# Exercício 3:  qual a Pessoa mais velha e quem pode dirigir
# Descrição: Faça um Programa que recebe um nome de duas pessoas e suas idades e diga qual a mais velha e qual pode dirigir veículos automotor.

# nome1 = (input("digite seu nome: "))
# idade1 = int (input("digite sua idade: "))
# nome2 = (input("digite seu nome: "))
# idade2 = int (input("digite sua idade: "))

# if idade1 > idade2:
#     if idade1 > 18:
#         print(f"{nome1} é mais velho que {nome2} e tem idade para dirigir")
#     else: print("nenhum dos dois pode dirigir")
# elif idade2 > idade1: 
#     if idade2 > 18:
#         print(f"{nome2} é mais velho que {nome1} e tem idade para dirigir")
#     else: print("nenhum dos dois pode dirigir")
# elif idade1 == idade2:
#     if idade1 > 18:
#         print("eles tem a mesma idade e os dois podem dirigir")
#     else:
#         print(f"a idade do {nome1} é igual a idade do {nome2} e ambos não podem dirigir")
# else: 
#     print("Os dados são inválidos")

# Exercício 4: Classificador de Idade
# Descrição: Crie um programa que solicite a idade de uma pessoa (um número inteiro).
# Se a idade for menor que 12, exiba "Criança".
# Se a idade estiver entre 12 e 17 (inclusive), exiba "Adolescente".
# Se a idade estiver entre 18 e 59 (inclusive), exiba "Adulto".
# Se a idade for 60 ou mais, exiba "Idoso".

# idade = int (input("Digite a sua idade: "))

# if idade < 12:
#     print("Criança")
# elif idade >= 12 and (idade <= 17):
#     print("Adolescente")
# elif idade > 18 and (idade < 59):
#     print("Adulto")
# else:
#     print("Idoso")


# Exercício 5: Calculadora Simples
# Descrição: Crie um programa que solicite dois números (reais) e uma operação matemática (+, -, *, /).
# Se a operação for "+", exiba a soma dos números.
# Se for "-", exiba a diferença.
# Se for "*", exiba o produto.
# Se for "/", verifique se o segundo número é diferente de zero. Se for, exiba o resultado da divisão; caso contrário, exiba "Erro: divisão por zero".
# Se a operação for diferente das anteriores mostre "Operação invalida"

numero1 = int (input("Digite um numero"))
operador = input (" +, -, *, /")
numero2 = int (input("Digite um numero")) 

# vai se fude tbm

if operador == "-":
    print("numero1 - numero2 = ") 


