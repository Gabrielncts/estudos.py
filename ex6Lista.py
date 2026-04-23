    #função para o menu
def menu() :
    print("\n lista de compras  ")
    print(" [1] adicionar item  ")
    print(" [2] remover item  ")
    print(" [3] visualizar itens  ")
    print(" [4] sair  ")
    #função para lista e criação de um array
lista = []
    #while "puxando" o menu
while True : 
    menu()
    escolhaMenu = int(input(" : "))
        #se a escolha for '1', o item será adicionado, usando "append"
    if escolhaMenu == 1 :
        item = input("Digite o item para adicionar: ")
        lista.append(item)
        print(f"Item {item}, foi adicionado ")
            #se for '2', o item vai ser removido, usando "remove"
    elif escolhaMenu == 2 :
        if item in lista : # "in" usado para localizar, se ITEM estiver em LISTA
            item = input("digite o item que será removido: ")
            lista.remove(item) # "remove" usado para remover
            print(f"Item {item}, removido ")
        else :
            print(f"Item {item}, não encontrado ")
                #mostrar a lista de itens adicionados
                #verifica se a lista está vazia antes
    elif escolhaMenu == 3 :
        print("\n Itens na lista: ")
        if not lista :
            print("A lista está vazia! ")
        else : 
                #enumerate para contar os itens
                #start para começar do numero 1
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
    elif escolhaMenu == 4 : 
        print("ENCERRANDO PROGRAMA.....")
        break #break para encerrar o programa
    else :
        print("OPÇÃO INVÁLIDA")
