# Função que recomenda o plano ideal com base no consumo informado
def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados (em GB)
consumo = float(input())
# Exibe a recomendação de plano ideal
print(recomendar_plano(consumo))

