"""
    Programa: Calculadora de Desconto
    Objetivo: Calcular o preço final de um produto
           após aplicar um desconto.
   Requisitos:
   a) Cálculo de desconto: calcula o valor do desconto 
   b) Preço final: determina o novo preço após o desconto
   c) Formatação: arredonda para 2 casas decimais 
   d) Interação: pede valores e mostra resultado formatado

"""

def parse_float_ptbr(texto: str) -> float:
    
    return float(texto.strip().replace(",", "."))


def calcular_valor_desconto(preco: float, desconto_percentual: float) -> float:
    """a - Calcula o valor do desconto (R$) baseado em uma porcentagem."""
    return preco * (desconto_percentual / 100)


def calcular_preco_final(preco: float, valor_desconto: float) -> float:
    """b - Determina o preço final após o desconto."""
    return preco - valor_desconto


def main() -> None:
    print("=== Calculadora de Preço com Desconto ===")

    # d - Interação com usuário: pede os valores necessários
    preco_produto = parse_float_ptbr(input("Digite o valor do produto:"))
    desconto_percentual = parse_float_ptbr(input("Digite o desconto percentualS: "))

    if preco_produto < 0:
        print("O valor do produto não pode ser negativo.")
        return

    if not (0 <= desconto_percentual <= 100):
        print("A porcentagem de desconto deve estar entre 0 e 100.")
        return

    # a - Cálculo de desconto
    valor_desconto = calcular_valor_desconto(preco_produto, desconto_percentual)

    # b - Preço final
    preco_final = calcular_preco_final(preco_produto, valor_desconto)

    # c - Formatação: Arredonda o resultado para 2 casas decimais (centavos)
    valor_desconto = round(valor_desconto, 2)
    preco_final = round(preco_final, 2)

    # d - Mostra o resultado formatado
    print("-" * 35)
    print(f"Preço original:    R$ {preco_produto:.2f}")
    print(f"Desconto aplicado: {desconto_percentual:.2f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final:       R$ {preco_final:.2f}")
    print("-" * 35)


if __name__ == "__main__":
    main()
