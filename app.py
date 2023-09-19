
def calcular_prestacao_em_atraso():
    try:
        valor_prestacao = float(input("Valor da prestação (em R$): "))
        taxa_juros = float(input("Taxa de juros por mês (%): "))
        dias_atraso = int(input("Número de dias de atraso: "))

        juros = (valor_prestacao * (taxa_juros / 100) * (dias_atraso / 30))

        valor_total = valor_prestacao + juros

        print(f"Juros a pagar: R$ {juros:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")
    except ValueError:
        print("Erro: Certifique-se de que os valores inseridos sejam numéricos.")

calcular_prestacao_em_atraso()

