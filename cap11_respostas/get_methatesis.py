import requests
import sys


def main():
    # pega lista de palavras na url
    url = "https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt"
    word_list = get_words_list(url)

    # monta dicionário de anagramas
    anagrams_dict = get_anagrams(word_list)

    # demonstra pro usuário os pares de metáteses
    get_list_methatesis(anagrams_dict)


# download from url and create list with words that will be the reference
def get_words_list(url):
    response = requests.get(url)
    word_list = response.text.splitlines()
    return word_list


# monta dicionário
def get_anagrams(word_list):
    '''
    Armazena em dict palavras que são anagramas
    Chave: string das letras que formam a palavra em ordem alfabética
    Valor: lista de palavras que contem as mesmas letras
    word_list: lista de palavras
    return: anagrams_dict
    '''
    anagrams_dict = {}

    # verifica cada palavra na lista
    for word in word_list:
        # consiga chave com caracteres ordenados
        key = sort_word(word)

        # se chave não está no dicionário, adicione-a com o valor
        if key not in anagrams_dict:
            anagrams_dict[key] = [word]
        # se chave já está no dicionário, adicione apenas o valor
        else:
            anagrams_dict[key].append(word)
    
    return anagrams_dict


# ordena as caracteres das palavras para ser chave do dicionário
def sort_word(word):
    '''Ordena as letras de uma palavra em ordem alfabética'''
    return ''.join(sorted(word))


# monta lista de metatesis
def get_list_methatesis(anagrams_dict):
    '''
    Pega dicionário com anagramas e verifica existencia de metéteses
    anagrams_dict: dicionário com listas de anagramas
    return: retorna lista com par de metáteses
    '''
    # pega cada lista de valores do dicionário
    for anagrams in anagrams_dict.values():
        # lista tem que ter comprimento mínimo de 2
        if len(anagrams) > 1:
            for i in range(len(anagrams)):
                word1 = anagrams[i]
                # se i é igual a última posição da lista, break
                if i + 1 == len(anagrams):
                    break

                for j in range(i+1, len(anagrams)):
                    word2 = anagrams[j]

                # se word_distance retornar 2
                if words_distance(word1, word2) == 2:
                    print(word1, word2)
                    
        

# calcula nº de posições com letras diferentes entre strings
def words_distance(word1, word2):
    """
    Calcula número de posições que duas strings diferem

    >>> word_distance("daniel", "danieu")
    1
    >>> word_distance("jordan", "jorela")
    2
    """
    # as duas palabas devem ter mesmo comprimento
    if len(word1) != len(word2):
        sys.exit("As palavras devem ter o mesmo comprimento")

    # conta letras diferentes por posição
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == "__main__":
    main()