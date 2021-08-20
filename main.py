import random
from algoritmos_ordenacao import *

# Controladores para criação da lista
lista = []
quantidade_de_chaves = 20000
limite_max_algarismo = 5000


def criar_lista():
    if not lista:
        # Criando da Lista
        for i in range(quantidade_de_chaves):
            lista.append(random.randint(1, limite_max_algarismo))
        separador()
        print(f'Lista Criada:\n', lista)
        separador()
    else:
        print('A lista já foi criada, caso queira altera-la delete a lista primeiro.')


def deletar_lista():
    if not lista:
        print(f'A lista já está vazia')
    else:
        # Apagando a Lista
        lista.clear()
    separador()
    print(f'Lista Deletada:\n', lista)
    separador()


while True:
    print(f'''
╔══════════════════════════╗
║           MENU           ║
║  (0) « Imprimir Lista »  ║
║  (1) « Criar Lista »     ║
║  (2) « Deletar Lista »   ║
║  (3) « Bubble Sort »     ║  
║  (4) « Insertion Sort »  ║      
║  (5) « Shell Sort »      ║ 
║  (6) « Merge Sort »      ║ 
║  (7) « Quick Sort »      ║
║  (8)  « Comparar »       ║
║  (9)   « Config »        ║
║  (X)    « Sair »         ║
╚══════════════════════════╝\n''')

    escolha = (input('Digita a opção escolhida: ').upper())
    if escolha == '0':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print(lista)
        continue

    elif escolha == '1':
        print('Criando uma lista...')
        criar_lista()
        continue

    elif escolha == '2':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Deletando a lista...')
            deletar_lista()
        continue

    elif escolha == '3':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Bubble Sort...')
            ordenar_bubble(lista)
        continue

    elif escolha == '4':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Insertion Sort...')
            ordenar_insertion(lista)
        continue

    elif escolha == '5':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Shell Sort...')
            ordenar_shell(lista)
        continue

    elif escolha == '6':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Merge Sort...')
            ordenar_merge(lista)
        continue

    elif escolha == '7':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Quick Sort...')
            ordenar_quick(lista)
        continue

    elif escolha == '8':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Comparando Algoritmos...')
            ordenar_bubble(lista)
            ordenar_insertion(lista)
            ordenar_shell(lista)
            ordenar_merge(lista)
            ordenar_quick(lista)
        continue

    elif escolha == '9':
        quantidade_de_chaves = int(input('Quantidade de Chaves da Lista\n (Padrão: 20000): '))
        limite_max_algarismo = int(input('Limite Máximo de Algarismo\n (Padrão: 5000): '))
        print('Configurações Salvas...')
        continue

    elif escolha == 'X':
        print('Finalizando o programa...')
        break

    else:
        print('Somente comandos disposto no MENU funcionam, boa tentativa meu chapa...')
