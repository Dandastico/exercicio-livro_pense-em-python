def read_head(input_name, n, output_name=None):
    # abrir arquivo de onde as linhas serão lidos
    reader = open(input_name, 'r')
    # se output_name tiver valor armazenado, abra outro arquivo
    if output_name:
        writer = open(output_name, 'w')
    
    # leia e escreva ou leia e demonstre ao usuário n linhas
    for _ in range(n):
        line = reader.readline()
        if output_name:
            writer.write(line)
        else:
            print(line, end='')

    # feche o arquivo de onde as linhas foram lidas
    reader.close()
    # feche o arquivo de saída se ele foi aberto
    if output_name:
        writer.close()


read_head("text.txt", 2, "output.txt")
read_head("text.txt", 2)