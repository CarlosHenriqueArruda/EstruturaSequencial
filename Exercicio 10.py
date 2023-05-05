'Informe o turno que você estuda, e receba uma saudação!'

turno=str(input("Que turno você estuda? Digite [M] para Matutino, [V] para Vespertino ou [N] para Noturno: "))
if turno == "M":
    print("Bom Dia!!!")
elif turno == "V":
    print("Boa Tarde!!!")
else:
    print("Boa Noite!!!")