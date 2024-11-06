lista = []
valores = []

def imprimeMenu():
    print('\n============================================')
    print('        Menu cardápio da casa:')
    print(65*'=')
    print('[1]- Feijão tropeiro_______________R$10,00')
    print('[2]- Feijoada______________________R$10,00')
    print('[3]- Feijão comum__________________R$7,50 ')
    print('[4]- Arroz comum___________________R$7,50 ')
    print('[5]- Lasanha_______________________R$10,50')
    print('[0]- Voltar')
    print(65*'=')
    print('Use os respectivos números que refere ao prato para adicionar')
    print(65*'=')

def menuOpcoes():
    print('\n============================================')
    print('O que deseja fazer? ')
    print(65*'=')
    print('[1]- Adicionar no prato')
    print('[2]- Remover do prato')
    print('[3]- Visualizar o prato')
    print('[0]- Sair')
    print(65*'=')

def imprimePedido():
    if len(lista) > 0:
        print(65*'-')
        print('Seu pedido:\n')
        cont = 0
        while cont < len(lista):
            print(f"{cont + 1} - {lista[cont]} - R$ {valores[cont]:.2f}".replace('.', ','))
            cont += 1
        print(65*'=')
    else:
        print(65*'=')
        print('\nVocê ainda não tem nenhum pedido!')
        print(65*'=')

while True:
    menuOpcoes()
    opcao = int(input('Opção desejada: '))
    if opcao == 1:
        while True:  
            imprimeMenu()
            opcaoPrato = int(input('Qual prato deseja adicionar: '))
            if opcaoPrato == 1:
                print('Feijão tropeiro adicionado ao prato')
                lista.append('Feijão tropeiro')
                valores.append(10.00)
                imprimePedido()
            elif opcaoPrato == 2:
                print('Feijoada adicionada ao prato')
                lista.append('Feijoada')
                valores.append(10.00)
                imprimePedido()
            elif opcaoPrato == 3:
                print('Feijão comum adicionado ao prato')
                lista.append('Feijão comum')
                valores.append(7.50)
                imprimePedido()
            elif opcaoPrato == 4:
                print('Arroz comum adicionado ao prato')
                lista.append('Arroz comum')
                valores.append(7.50)
                imprimePedido()
            elif opcaoPrato == 5:
                print('Lasanha adicionada ao prato')
                lista.append('Lasanha')
                valores.append(10.50)
                imprimePedido()
            elif opcaoPrato == 0:
                print('\nRetonando ao menu de opções\n')
                break
            else:
                print('\nOpção inválida.')

    elif opcao == 2:
        if len(lista) > 0:
            print(65*'-')
            print('Seu pedido:\n')
            cont = 0
            while cont < len(lista):
                print(f"{cont + 1} - {lista[cont]} - R$ {valores[cont]:.2f}".replace('.', ','))
                cont += 1
            print(65*'=')
            remover = int(input('Digite a opção que deseja remover: '))
            if remover > 0 and remover <= len(lista):
                item_removido = lista[remover-1]
                del lista[remover-1]
                del valores[remover-1]
                print(f"{item_removido} removido do pedido.")
            else:
                print('Opção inválida')
        else:
            print(65*'-')
            print('\nVocê ainda não tem nenhum pedido!')
            print(65*'-')
            
    elif opcao == 3:
        imprimePedido()

    elif opcao == 0:
        if len(lista) > 0:
            print('Seu pedido:\n')
            total = 0
            cont = 0
            while cont < len(lista):
                print(f"{cont + 1} - {lista[cont]} - R$ {valores[cont]:.2f}".replace('.', ','))
                total += valores[cont]
                cont += 1
            print(f'\nTotal__________________R$ {total:.2f}\n'.replace('.', ','))
            print(65*'=')
            print('Obrigado pela preferência, volte sempre!!!')
            print(65*'=')
            break
        else:
            print(65*'=')
            print("Você não consumiu nada.")
            print("Obrigado pela preferência, volte sempre!!!")
            print(65*'=')
            break

    else:
        print("\nEscolha uma opção valida por favor.")
