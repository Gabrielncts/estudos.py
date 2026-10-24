#entrada de dados com float
print("------calcular media ponderada da materia -------")
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))
#definicao dos pesos e calculo da media ponderada
peso1 = 1
peso2 = 2
peso3 = 3
nota1 = (nota1 * 1)
nota2 = (nota2 * 2)
nota3 = (nota3 * 3)
mediaP = (nota1 + nota2 + nota3) / (peso1 + peso2 + peso3)
print(f"A media ponderada e {mediaP: .2}")
