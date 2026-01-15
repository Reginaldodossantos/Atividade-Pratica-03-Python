"""
 Dias de Vida
 Calcular quantos dias a pessoa está viva
 usando a data de hoje automaticamente.
"""

from datetime import date


def calcular_dias_de_vida(data_nascimento: date) -> int:
    """
    Calcula a quantidade de dias entre a data de nascimento e a data atual.

    Retorna:
    int: número de dias de vida
    """
    return (date.today() - data_nascimento).days


def main() -> None:
    hoje = date.today()

    while True:
        try:
            print("Digite sua data de nascimento:")
            dia = int(input("Dia (1-31): ").strip())
            mes = int(input("Mês (1-12): ").strip())
            ano = int(input("Ano (ex: 2002): ").strip())
            nascimento = date(ano, mes, dia)

            if nascimento > hoje:
                print("\nErro: a data de nascimento não pode ser no futuro. Tente novamente.\n")
                continue

            dias = calcular_dias_de_vida(nascimento)

            print("\nResultado")
            print("-------------------")
            print(f"Data de nascimento: {nascimento.strftime('%d/%m/%Y')}")
            print(f"Data de hoje: {hoje.strftime('%d/%m/%Y')}")
            print(f"Dias de vida: {dias} dias")
            break

        except ValueError:
            print("\nErro: data inválida (ex.: 31/02) ou entrada não numérica. Tente novamente.\n")


if __name__ == "__main__":
    main()
