# Leia a temperatura atual do usuário
temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

# Avalie a temperatura e exiba a mensagem apropriada
if temperatura < 7:
    print("Comgelado")
elif temperatura < 10:
    print("Frio")
elif temperatura < 26:
    print("Ótimo")
else:
    print("Quente")
