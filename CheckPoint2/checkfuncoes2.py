import time

def cadastrar(info):
    tpm = 's'
    while tpm == 's':
        nome = input('Entre com um nome: ').lower()  
        info[nome]= [input('\nColoque um Email: '), input('Senha do Email: ')]
        tpm = input('\nDeseja cadastrar novamente?(S ou N): ').lower()


def exibir(info):
    for key, dicio in info.items():
        print('---------------------------------')
        print("Nome =>", key)
        print("\nEmail => ", dicio[0])
        print("Senha => ", dicio[1])
    print('---------------------------------')
    input('\nPressione ENTER para voltar ao menu')

def buscar(info):
    busca = input("Digite um nome para checagem: ").lower()
    if info.get(busca) != None:
        dicio = info.get(busca)
        print("\nEmail =>", dicio[0])
        print("Senha =>", dicio[1])
        input('\nPressione ENTER para voltar ao menu')

def alterar(info):
    while True:
        print('''
    +--------------------+
    | Menu De Alteração  |
    +--------------------+
    |1 => Email          |
    |2 => Senha          |
    |3 => Email e Senha  |
    |4 => Sair           |
    +--------------------+
        ''')
        alterar = input('Oque deseja alterar?(1-4): ')
        if alterar.isdigit():
            alterar = int(alterar)
            if alterar == 1:
                email = input('Qual o nome da pessoa que deseja alterar o email? ').lower()
                if info.get(email) != None:
                    lista = info.get(email)
                    info[email]= [input('insira novo email: '), lista[1]]
                    print('Email alterado com sucesso')
                    time.sleep(1)
                else:
                    print('Essa pessoa não existe nos registros.')
            elif alterar == 2:
                senha = input('Qual o nome da pessoa que deseja alterar a senha? ').lower()
                if info.get(senha) != None:
                    lista = info.get(senha)
                    info[senha]= [lista[0], input('Insira senha nova: ')]
                    print('Senha alterada com sucesso')
                    time.sleep(1)
                else:
                    print('Essa pessoa não existe nos registros.')
            elif alterar == 3:
                nome = input('Qual o nome da pessoa que deseja alterar? ').lower()
                if info.get(nome) != None:
                    lista = info.get(nome)
                    info[nome]= [input('Insira novo email: '), input('Insira senha nova: ')]
                    print('As informações foram altedaras com sucesso')
                    time.sleep(1)
                else:
                    print('Essa pessoa não existe nos registros.')
            elif alterar == 4:
                break
            else:
                print('\nVocê só tem quatro alternativas, não deve ser tão dificil assim')
        else:
            print('\nIsso não é um numero')

def excluir(info):
    excluir = input("Nome para excluir: ").lower()
    if info.get(excluir) != None:
        del info[excluir]
        print(f'\nO dados do nome "{excluir}" foram excluidos')
        time.sleep(1)
    else:
        print('Nome não encontrado')
        time.sleep(1)

def carregamento(tam):
    print("\rCarregando: [{0:50}] {1:.0f}%".format('#' * int(tam * 50), tam * 100),end='')
