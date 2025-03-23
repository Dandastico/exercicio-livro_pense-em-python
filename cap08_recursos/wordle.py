def main():
    tries = 6
    target = "afeto"
    
    for i in range(tries):
        guess = input(f"{i+1}ª tentativa: ")
        if wordle(target, guess):
            print(f"Você acertou na {i}ª tentativa!")
            break
        else:
            pass


def wordle(target, guess):
    """
    Função que verifica se  a plavavra adivinhada é correta
    Se não for certo, verifica se os caracteres estão corretos
    Se o caractere for correto, verifica se está na posição certa
    """
    # usuário acertou a palavra
    if target == guess:
        return True
    




if __name__ == "__main__":
    main()