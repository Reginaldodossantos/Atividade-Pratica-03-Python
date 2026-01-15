"""

     Programa: Verificador de Palíndromo
     Objetivo: Verificar se uma palavra/frase é palíndromo,
     ignorando espaços e pontuação.

"""

def normalizar_texto(texto: str) -> str:
    """
    Remove caracteres que não são letras/números e converte para minúsculas.
    """
    return "".join(c.lower() for c in texto if c.isalnum())


def eh_palindromo(texto: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente),
    ignorando espaços e pontuação.

    Retorna:
    bool: True se for palíndromo, False caso contrário.
    """
    texto_limpo = normalizar_texto(texto)
    return texto_limpo == texto_limpo[::-1]


def main() -> None:
    entrada = input("Digite uma palavra ou frase: ").strip()

    resultado = eh_palindromo(entrada)
    # True -> "Sim" o
    # False -> "Não"

    print("Sim" if resultado else "Não")

    # Comentário com valor final esperado 
    # Entrada: "A base do teto desaba"  -> Sim
    # Entrada: "Olá mundo"             -> Não


if __name__ == "__main__":
    main()
