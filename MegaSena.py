import random


def sorteia():
    lista_numeros = []
    for i in range(1, 61):
        lista_numeros.append(i)

    cont = 1
    aposta = []
    while cont <= 6:
        random.shuffle(lista_numeros)
        num = lista_numeros[0]
        if num not in aposta:
            aposta.append(num)
            cont += 1
    return sorted(aposta)


def escolhe():
    with open('antigos.txt', 'r') as file:
        arq = file.read()

    antigos = list(arq.split('\n'))
    sorteado = sorteia()
    for linha in antigos:
        if linha == sorteado:
            print("Repetido:", linha, sorteado)
            return False, ''
    return True, sorteado


def define_aposta():
    print('')
    cont = 0
    while cont < 4:
        while True:
            escolhido = escolhe()
            if escolhido[0]:
                print(escolhido[1])
                break

        cont += 1
    print('')
        

try:
    num_ap = int(input('Esse programa gera um conjunto de 4 apostas.\nQuantos conjuntos você quer gerar?\n'))
    if num_ap == 1:
        define_aposta()
    else:
        while num_ap > 0:
            define_aposta()
            num_ap -= 1
    pausa = input('Pressione "Enter" para encerrar')
except:
    define_aposta()
    pausa = input('Pressione "Enter" para encerrar')
