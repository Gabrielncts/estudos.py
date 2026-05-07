agenda = {}
def addContato() :
    nome = input("Digite o nome: ")
    tel = int(input("telefone (APENAS NÚMEROS): "))
    email = input("Digite o email: ")
    agenda[nome] = {
        "telefone" : tel,
        "email" : email
    }
    print(f"Contato {nome}, adicionado com sucesso!")
def buscaContato() :
    print("digite o nome do contato para pesquisa: ")
    nome = input(" : ")
    if nome in agenda :
        print(f"Contato encontrado: {nome}")
        print(f"Telefone: {agenda[nome]['telefone']}")
        print(f"Email: {agenda[nome]['email']}")
    else :
        print("CONTATO NÃO ENCONTRADO")
def listaContato() :
    if not agenda :
        print("A agenda está vazia")
    else :
        for i, (nome, info) in enumerate(agenda.items(), start=1) :
            print(f"{i}. {nome} - Telefone: {info['telefone']} - Email: {info['email']}")
def menu() :
    print("agenda de contatos")
    print("[1] adicionar contato")
    print("[2] buscar contato")
    print("[3] listar contatos")
    print("[4] SAIR")


while True :
    menu()
    escolhaMenu = int(input(" : "))
    if escolhaMenu == 1 :
        addContato()
    elif escolhaMenu == 2 :
        buscaContato()
    elif escolhaMenu == 3 :
        listaContato()
    elif escolhaMenu == 4 :
        print("Fechando programa. . . . ")
        break
    else :
        print("Escolha uma opção válida")