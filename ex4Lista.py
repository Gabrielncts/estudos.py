numero = int(input("Insira um numero para a tabuada: "))
print(f"Tabuada do numero: ", numero)
for i in range(1, 11) :
    print(f"{numero} x {i} = {numero * i}")