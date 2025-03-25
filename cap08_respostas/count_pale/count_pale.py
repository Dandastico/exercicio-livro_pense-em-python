import re


def main():
    count = count_pale()
    print(count)


def count_pale():
    """
    Função conta quantas vezes a palavra "pale" e seus derivados
    se repetem no arquivo texto
    """
    pattern = r"\bpale(?:s|d|ness)?\b|\bpallor\b"
    count = 0
    for line in open("text.txt"):
        line = line.lower()
        result = re.findall(pattern, line)
        if result != None:
            count += 1
    return count


if __name__ == "__main__":
    main()