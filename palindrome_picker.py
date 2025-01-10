# Verificador de Palíndromo

def verificar_palindromo():
    print("=== Verificador de Palíndromos ===")
    texto = input("Digite uma palavra ou frase: ").strip().lower()

    # Remove espaços e caracteres não alfabéticos
    texto_limpo =  ''.join(char for char in texto if char.isalnum())

    # Verifica se o texto limpo é um palíndromo
    if texto_limpo == texto_limpo[::-1]:
        print(f"'{texto}' é um palíndromo!")
    else:
        print(f"'{texto}' não é um palíndromo.")

if __name__ == "__main__":
    verificar_palindromo()
