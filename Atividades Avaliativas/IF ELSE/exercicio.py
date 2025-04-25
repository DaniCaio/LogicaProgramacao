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

# print("\n selecione a sua operação: ")
# print("(-) - subtração")
# print("(+) - soma")
# print("(/) - divisão")
# print("(*) - multiplicação")

# operador = input("Digite o operador: ")

# if operador == "-":
#     numero1 = float (input("Digite o primeiro número: "))
#     numero2 = float (input("Digite o segundo número: ")) 

#     resultado = numero1 - numero2
#     print(resultado)
# elif operador == "+":
#     numero1 = float (input("Digite o primeiro número: "))
#     numero2 = float (input("Digite o segundo número: ")) 

#     resultado = numero1 + numero2
#     print(resultado)
    
# elif operador == "/":
#     numero1 = float (input("Digite o primeiro número: "))
#     numero2 = float (input("Digite o segundo número: ")) 
    
#     if numero2 == 0:
#         print("Erro: divisão por zero.")

#     else:
#         resultado = numero1 / numero2
#         print(resultado)

# elif operador == "*":
#     numero1 = float (input("Digite o primeiro número: "))
#     numero2 = float (input("Digite o segundo número: ")) 

#     resultado = numero1 * numero2
#     print(resultado)

# else:
#     print("A opção escolhida é invalida.")

# xercício 6: Verificador de Números Positivos, Negativos e Zeros
# Descrição: Crie um programa que solicite um número real ao usuário.
# Se o número for maior que 0, exiba "Positivo".
# Se for menor que 0, exiba "Negativo".
# Se for igual a 0, exiba "Zero".

# numero = input ("Digite um número real")

# if numero > 0:
#     print("Positivo")

# elif numero < 0:
#     print("Negativo")

# else:
#     print("Zero")

# Exercício 7: Cálculo do IMC
# Descrição: Crie um programa que solicite o peso (em kg) e a altura (em metros) de uma pessoa.
# Calcule o IMC (IMC = peso / altura²).
# Se o IMC for menor que 18.5, exiba "Abaixo do peso".
# Se o IMC estiver entre 18.5 e 24.9 (inclusive), exiba "Peso normal".
# Se o IMC estiver entre 25 e 29.9 (inclusive), exiba "Sobrepeso".
# Se o IMC for 30 ou maior, exiba "Obesidade".

# peso = float (input ("Digite seu peso em KG "))
# altura = float (input ("Digite sua altura em metros "))

# IMC = peso / (altura ** 2) 

# if IMC < 18.5:
#     print(f"Abaixo do peso {IMC}")

# elif IMC >= 18.5 and ( IMC <= 24.9):
#     print(F"Peso normal {IMC}")

# elif IMC >= 25 and ( IMC <=29.9):
#     print(F"Sobrepeso {IMC}")

# else:
#     print(F"Obesidade {IMC}")

# Exercício 8: Verificador de Ano Bissexto
# Descrição: Crie um programa que solicite um ano (número inteiro).
# Um ano é bissexto se for divisível por 4, exceto anos divisíveis por 100 que não são divisíveis por 400.
# Se o ano for bissexto, exiba "Ano bissexto"; caso contrário, exiba "Ano não bissexto".

# ano = int (input("Digite um ano: "))

# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("bissexto")

# else:
#     print("ano não bissexto")

# Exercício 9: Conversor de Temperatura
# Descrição: Crie um programa que solicite uma temperatura e a escala original (Celsius ou Fahrenheit).
# Se a escala for "C", converta para Fahrenheit (F = C * 9/5 + 32).
# Se a escala for "F", converta para Celsius (C = (F - 32) * 5/9).
# Caso a escala seja diferente de "F" ou "C" mostre "Escala invalida".
    
# temperatura = float (input("Digite uma temperatura: "))

# print("\n Selecione a escala: ")
# print("C - Celsius")
# print("F - Fahrenheit")

# escala = input ("Digite a letra correspondente a escala: ")

# if escala == "C":
#     fahrenheit = temperatura * 9/5 + 32
#     print(f"Sua temperatura em fahrenheit é {fahrenheit}")

# elif escala == "F":
#     celsius = (temperatura - 32) * 5/9
#     print(f"Sua temperatura em celsius é {celsius}")

# else:
#     print("Escala invalida")
    

