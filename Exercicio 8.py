"Verificar se uma Letra é Vogal ou Consoante"

Letra = str(input("Digite a letra: ")).title()
if Letra in "AEIOU":
    print("Vogal")
else:
    print("Consoante")