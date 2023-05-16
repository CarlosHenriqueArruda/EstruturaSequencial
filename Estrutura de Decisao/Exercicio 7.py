#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar.
#Sabendo que a decisão é sempre pelo mais barato.
numero1 = float(input("Digite o preço do primeiro produto: "))
numero2 = float(input("Digite o preço do segundo produto: "))
numero3 = float(input("Digite o preço do terceiro produto: "))
if numero1 < numero2 and numero1 < numero3:
    print(f"O numero {numero1} é o menor preço..")
elif numero2 < numero1 and numero2 < numero3:
    print(f"O numero {numero2} é o menor preço..")
else:
    print(f'O numero {numero3} é o menor preço.')