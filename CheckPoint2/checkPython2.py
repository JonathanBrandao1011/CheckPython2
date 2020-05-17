from checkfuncoes2 import *

print(r'''
  ______ ______ _____  _____            __  __ ______ _   _ _______         _    _          _____ _  ________ _____  
 |  ____|  ____|  __ \|  __ \     /\   |  \/  |  ____| \ | |__   __|/\     | |  | |   /\   / ____| |/ /  ____|  __ \ 
 | |__  | |__  | |__) | |__) |   /  \  | \  / | |__  |  \| |  | |  /  \    | |__| |  /  \ | |    | ' /| |__  | |__) |
 |  __| |  __| |  _  /|  _  /   / /\ \ | |\/| |  __| | . ` |  | | / /\ \   |  __  | / /\ \| |    |  < |  __| |  _  / 
 | |    | |____| | \ \| | \ \  / ____ \| |  | | |____| |\  |  | |/ ____ \  | |  | |/ ____ \ |____| . \| |____| | \ \ 
 |_|    |______|_|  \_\_|  \_\/_/    \_\_|  |_|______|_| \_|  |_/_/    \_\ |_|  |_/_/    \_\_____|_|\_\______|_|  \_\
''')



for n in range(28):
    carregamento(n/27)
    time.sleep(0.1)
dic = {'lucas':['lukinhas.gamer@gmail.com', 'lukinhas123'],
    'fernanda':['fenanda2010@hotmail.com', 'nanda04458'],
    'joao':['joaocarlos@gmail.com', 'jaozin123']
}

while True:
    print('''\n
    +--------------------+
    | Menu De Vazamentos |
    +--------------------+
    |1 => Cadastrar      |
    |2 => Exibir Todos   |
    |3 => Alterar        |
    |4 => Buscar         |
    |5 => Excluir        |
    |6 => Sair           |
    +--------------------+
        ''') 
    escolha = input('\nEscolha uma das Opções(1-6): ')
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            cadastrar(dic)
        elif escolha == 2:
            exibir(dic)
        elif escolha == 3:
            alterar(dic)
        elif escolha == 4:
            buscar(dic)
        elif escolha == 5:
            excluir(dic)
        elif escolha == 6:
            break
        else:
            print('\nApenas numeros entre 1 e 6')
            time.sleep(2)
    else:
        print('\nPor favor selecione um numero')
