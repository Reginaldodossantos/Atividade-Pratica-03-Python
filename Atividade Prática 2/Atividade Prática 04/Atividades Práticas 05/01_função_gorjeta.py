# ============================================
# Programa: Calculadora de Gorjeta
# Objetivo: Calcular o valor da gorjeta com base no total da conta
#           e na porcentagem desejada.
# ============================================


def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): A porcentagem da gorjeta

    Retorna:
        float: O valor da gorjeta calculada
    """
    return valor_conta * (porcentagem_gorjeta / 10)


def cliente_quer_remover_gorjeta() -> bool:
    """
    Pergunta ao usuário se deseja remover a gorjeta.

    Retorna:
        bool: True se o usuário digitar "sim", False caso contrário.
    """
    resposta = input("\nDeseja remover a gorjeta? (sim/não): ").strip().lower()
    return resposta == "sim"


def main() -> None:
    # Valores fixos para o cálculo solicitado
    valor_conta = 275.00

    # Opções de taxa de serviço (mínimo e máximo)
    porcentagem_minima = 12.0
    porcentagem_maxima = 17.0

    # Cálculos para a porcentagem mínima (12%)
    gorjeta_min = calcular_gorjeta(valor_conta, porcentagem_minima)
    total_min = valor_conta + gorjeta_min

    # Cálculos para a porcentagem máxima (17%)
    gorjeta_max = calcular_gorjeta(valor_conta, porcentagem_maxima)
    total_max = valor_conta + gorjeta_max

    # Exibição dos resultados
    print("\nCalculadora de Gorjeta")
    print("----------------------")
    print(f"Valor da conta: R$ {valor_conta:.2f}")

    print("\nOpção 1 (mínimo):")
    print(f"Porcentagem da gorjeta: {porcentagem_minima:.2f}%")
    print(f"Valor da gorjeta: R$ {gorjeta_min:.2f}")
    print(f"Total com gorjeta: R$ {total_min:.2f}")

    print("\nOpção 2 (máximo):")
    print(f"Porcentagem da gorjeta: {porcentagem_maxima:.2f}%")
    print(f"Valor da gorjeta: R$ {gorjeta_max:.2f}")
    print(f"Total com gorjeta: R$ {total_max:.2f}")

    # Pergunta se o cliente quer remover a gorjeta
    if cliente_quer_remover_gorjeta():
        print("\nGorjeta removida com sucesso!")
        print(f"Total sem gorjeta: R$ {valor_conta:.2f}")
    else:
        print("\nGorjeta mantida. Obrigado!")


"""
    Fiz um teste deixando com 2 opções de gorjeta e caso o cliente 
    não queira acrescentar o valor cobrado!

"""

if __name__ == "__main__":
    main()
