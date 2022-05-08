
def carregarVariaveis():
    arquivo = open("entrada.txt","r")
    primeira_linha = arquivo.readline().split('|')
    segunda_linha = []

    for linha in arquivo:
        arr = linha.split('|')
        if len(arr) > 1:
            segunda_linha = arr

    if len(primeira_linha) != 11 or len(segunda_linha) != 11:
        print('arquivo invalido')
        pass

    entrada = {}
    for i in range(11):
        if primeira_linha[i] != "" and segunda_linha[i] != "":
            entrada[primeira_linha[i].replace('\n','')] = segunda_linha[i]
        else:
            print('arquivo invalido')
            pass
    return entrada


