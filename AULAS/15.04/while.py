
nome = input("Digite seu nome: ") 

while True:
    # While True faz com que o loop não encerre mesmo que seja verdadeiro ou falso, mesmo que o input solicitado esteja errado. Somente encerrando com o break.
    # Try executa essa informação e se estiver incorreto leva para o except, causo esteja correto executa o codigo dentro dele.
    try:
        idade=int(input(f"Digite idade de {nome}: "))
        break
    # Except serve para que quando ocorrer um erro no try, (codigo usado em conjunto com try) ele execute o que esta dentro de except, evitando que de problemas e gere erros.
    except:
        print("Criatura Digite um numero inteiro")
print(f"{nome } tem {idade} anos de idade")


print('Digite as 12 temperaturas médias de cada mês do ano')
print('Para calcularmos a média do ano')
# variável acumuladora inicializada com ZERO
# para somar todas temperaturas do ano
soma=0
# repetição para interar 12 vezes equivalentes aos
# meses do ano
for mes in range (1,13):
    # loop para verificar se não Houve ERRO na digitação
    # Enquanto tiver erro NÃO sai do while
    while True:
        #controle de erro
        try:
            temp=float(input(f'Digite temperatura do mês {mes}:'))
            while temp <-70 or temp > 60:
                print("Temperatura fora dos limites aceitaveis")
                temp=float(input(f"Digite Novamente temperatura do mês:{mes} "))
            soma+=temp
            # SAI quando OK
            break
        #trata ERRO informa mensagem
        except:
            print("\n ***** DIGITE TEMPERATURA FLOAT ******\n")
    #volta próxima interação mês 
#fim do FOR
print(f'Media do ANo {(soma/12):.2f}')

