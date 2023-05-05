'Informe o preço de 3 produtos e veja qual o mais barato'

prod1 = float(input("Informe o preço do primeiro produto: "))
prod2 = float(input("Informe o preço do segundo produto: "))
prod3 = float(input("Informe o preço do terceiro produto: "))

if prod1 < prod2 and prod1< prod3:
    print(f'Você deve comprar o primeiro produto por R${prod1}')
elif prod2 < prod1 and prod2< prod3:
    print(f'Você deve comprar o segundo produto por R${prod2}')
else:
    print(f'Você deve comprar o segundo produto por R${prod3}')