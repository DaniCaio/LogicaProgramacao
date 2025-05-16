# lista=[7,303,"Senac","mouse",17.5,8]
# # Coloca em elemento cada opção da lista, e depois imprimi cada 1 deles.
# for elemento in lista:
#     print(elemento)
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])
# print(lista[5])
# print("#"*25)
# for i in range(6):
#     print(lista[i])

# print("#"*25)
# lista[4]="J"
# print(lista)

frutas=["maça","morango","banana"]

print("frutas")
while True:
    elemento=input("Digite uma fruta: ")
    if elemento.upper() == "FIM":
        break
    frutas.append(elemento)

print(frutas)
for elemento in frutas:
    print(elemento)
    frutas.insert(3,"abacaxi")
    print(elemento)
    break

print(frutas)

