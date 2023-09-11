# aula1-python

![Captura de tela 2023-09-10 214018](https://github.com/marcosaureliosl/aula1-python/assets/127764997/44187c45-ea2e-49e0-9e5c-feadab27359f)

## MInhas primeiras linhas de python

Programa de console para calcular a prestação em atraso da seguinte forma:

```python
# Função para calcular a prestação em atraso
def calcular_prestacao_em_atraso():
    try:
        valor_prestacao = float(input("Valor da prestação (em R$): "))
        taxa_juros = float(input("Taxa de juros por mês (%): "))
        dias_atraso = int(input("Número de dias de atraso: "))

        # Calcular juros
        juros = (valor_prestacao * (taxa_juros / 100) * (dias_atraso / 30))

        # Calcular valor total
        valor_total = valor_prestacao + juros

        # Exibir resultados
        print(f"Juros a pagar: R$ {juros:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")
    except ValueError:
        print("Erro: Certifique-se de que os valores inseridos sejam numéricos.")

# Chamada da função para calcular a prestação em atraso
calcular_prestacao_em_atraso()
```

Este código Python permite que o usuário insira os valores da prestação, da taxa de juros e do número de dias de atraso no console. Em seguida, ele calcula os juros a serem pagos e o valor total da prestação com os juros e exibe os resultados no console. Certifique-se de que você tenha o Python instalado em seu sistema para executar este programa.
