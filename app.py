print("bem vindo a Calculaddora teste PY")
print("Insira aqui 2 numeros inteiros: ")
numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))
print("qual operação gostaria de realizar? ")
print(" 1 - soma")
print(" 2 - subtração")
print(" 3 - divisão")
print(" 4 - multiplicação")
escolha = int(input(": "))
if (escolha == 1):
    numero3 = int(numero1 + numero2)
    print("soma = ", numero3)
elif (escolha == 2):
    numero3 = int(numero1 - numero2)
    print("subtração = ", numero3)
elif (escolha == 3):
    numero3 = int(numero1 / numero2)
    print("divisão = ", numero3)
else:
    numero3 = int(numero1 * numero2)
    print("multiplicação = ", numero3)
    
