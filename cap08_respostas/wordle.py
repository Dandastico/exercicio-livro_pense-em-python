def main():
    tries = 6
    target = "afeto"
    print("---------- WORDLE ----------")
    print("Regras:\n1- Você precisa acertar a palavra em até 6 tentativas")
    print("2- A palavra-alvo tem 5 letras, seu chute também deve ter 5 letras")
    print("3- Se um 'V' aparecer embaixo da letra, ela está correta na posição correta")
    print("4- 'A' significa que a letra está correta, mas na posição errada")
    for i in range(tries):
        guess = input(f"{i+1}ª tentativa: ").lower()
        if wordle(guess, target):
            print(f"Você acertou na {i+1}ª tentativa!")
            break
        


def wordle(guess, target):
    """
    Função que verifica se  a plavavra adivinhada é correta
    Se não for certo, verifica se os caracteres estão corretos
    Se o caractere for correto, verifica se está na posição certa
    """
    print(guess)
    for i in range(len(guess)):
        # caractere correta e mas na posição errada
        if guess[i] in target and guess[i] != target[i]:
            print("A", end='')
        # caractere está correta na posição correta
        elif guess[i] in target and guess[i] == target[i]:
            print("V", end='')
        # caractere errado
        else:
            print(' ', end='')
    print()
    # usuário acertou a palavra
    if target == guess:
        return True
    
    return False


if __name__ == "__main__":
    main()