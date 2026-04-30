print(" LOCALIZADOR DE VOGAIS ")
palavra = input("digite uma palavra: ").lower()
vogais = 'aeiou'
#for usado para verificar letra por letra da palavra digitada;
encontrou = False
for letra in palavra :
    if letra in vogais :
        print(f"A vogal '{letra}' foi encontrada na palavra")
        encontrou = True
if not encontrou :
    print("palavra não possui vogal")
