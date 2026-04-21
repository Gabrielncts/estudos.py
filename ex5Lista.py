print("CALCULADOR DE MEDIA DE NOTAS ")
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insita a terceira nota: "))
media = ((nota1 + nota2 + nota3) / 3)
print("MEDIA: ", media)
if (media >= 7) :
    print(" APROVADO ")
else :
    print(" REPROVADO ")