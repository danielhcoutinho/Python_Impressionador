import json
import time
import os

compras = {}

def adicionar_item(compras, item, quantidade):
        compras[item] = quantidade #add no dic compras a chave (item) e o valor (quantidade)

def remover_item(compras, item):
    if item in compras: #se tiver o item em compras
        del compras[item] #deleta o item do dic compras

def visualizar_compras(compras):
    for item, quantidade in compras.items(): #para cada item/quantidade nos itens do dic compras
         print(f'{item}: {quantidade}') #printar o item e a quantidade dele
    print()
    print('Pressione enter para continuar')
    input()

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo: #abre um arquivo para escrita para outro novo arquivo
        json.dump(compras, arquivo) #passamos o dic (compras) para o arquivo

def carregar_compras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo: #abre um arquivo para leitura para o outro novo arquivo
        return json.load(arquivo) #carrega o arquivo passado

def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #serve para limpar a tela dependendo do terminal que usa cls ou clear

        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        escolha = input('Escolha uma opção')

        if escolha == '1':
            item = input('Digite o nome do item: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionar_item(compras, item, quantidade)

        elif escolha == '2':
            item = input('Digite o nome do item: ')
            remover_item(compras, item)

        elif escolha == '3':
            visualizar_compras(compras)

        elif escolha == '4':
            if nome_arquivo is None: # se for nada no nome (se nao tem esse arquivo)
                nome_arquivo = input('Digite o nome do arquivo para salvar:') #digitamos o nome do arquivo
            if not nome_arquivo.endswith('.json'): #se nao termina com '.json'
                nome_arquivo += '.json' #pega o nome do arquivo e acrescenta o ".json"
            salvar_compras(compras, nome_arquivo) #salvamos a dic (compras) dentro do arquivo
            break

        elif escolha == '5':
            break
        else:
            print('Opção invalida')
            time.sleep(1)

def main():
    while True: #enquanto verdadeiro / enquanto nao sair 
        os.system('cls' if os.name == 'nt' else 'clear') #serve para limpar a tela dependendo do terminal que usa cls ou clear

        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)

        elif escolha == '2':
            print('Listas Disponiveis:')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')] # percorre cada arquivo e recebe apenas aquele que termina com '.json'
            if not arquivos: #se nao tiver arquivo ou nao termina com '.json'
                print('Nenhuma lista encontrada')
                time.sleep(3)
                continue
            for i, arquivo in enumerate(arquivos, 1): #para cada indice e arquivo em arquivos e numero 1
                print(f'{i} {arquivo}') #printa o n° do arquivo e o nome
            escolha = int(input('Escolha uma lista (0 se nenhuma): '))
            if escolha == 0: #se escolha for igual a 0
                continue
            elif escolha < 0 or escolha > len(arquivos): #se for menor que 0 ou  maior que o n° de arquivos existentes
                print('Opção invalida')
                time.sleep(1)
                continue
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo) #definimos a lista com a funcao carregar compras com o arquivo passado acima

            gerenciar_compras(compras, nome_arquivo) #passamos para a funçao a lista e o arquivo

        elif escolha == '3': #se escolher 3
            break #para o loop, para o cod ou retorna do menu
        else:
            print('Opção invalida')
            time.sleep(1)

if __name__ == "__main__":
    main()