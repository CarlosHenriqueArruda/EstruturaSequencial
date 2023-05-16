#Faça um Programa que leia três números e mostre o maior deles.
numero1 = int(input("Digite o primeiro numero: "))
numero2= int(input("Digite o segundo numero: "))
numero3= int(input("Digite o terceiro numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"O numero {numero1} é o maior.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O numero {numero2} é o maior.")