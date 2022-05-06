AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>> Não existe contatos para mostrar!')

def buscar_contato(contato):
    try:
        print("-----------------------------------------------")
        print("Nome: {}".format(contato))
        print("Telefone: {}".format(AGENDA[contato]['tel']))
        print("E-mail: {}".format(AGENDA[contato]['email']))
        print("Endereço: {}".format(AGENDA[contato]['endereco']))
        print("-----------------------------------------------")
    except KeyError:
        print('>>>> Esse contato não existe')
    except Exception as error:
        print('>>>> Um erro inesperado aconteceu')

def ler_detalhes():
    tel = input('Telefone: ')
    email = input('E-mail: ')
    endereco = input('Endereço: ')
    return tel, email, endereco

def incluir_editar_contato(contato, tel, email, endereco):
        AGENDA[contato] = {
            'tel': tel,
            'email': email,
            'endereco': endereco
        }


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        exportar_contatos()
        print("-----------------------------------------------")
        print(">>>>>> Contato {} Excluido Com Sucesso!!".format(contato))
        print("-----------------------------------------------")
        print("\n")
    except KeyError:
        print('>>>> Esse contato não existe')
    except Exception as error:
        print('>>>> Um erro inesperado aconteceu')

def exportar_contatos():
    nome_do_arquivo = 'database.csv'
    try:
        with open(nome_do_arquivo, 'w') as file:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write('{},{},{},{}\n'.format(contato, tel, email, endereco))
        print('>>>> Agenda exportada com sucesso!')
    except Exception as e:
        print('>>>> Algum erro ocorreu', e)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as file:
            imports = file.readlines()
            for linha in imports:
                contato = linha.strip().split(',')
                nome = contato[0]
                tel = contato[1]
                email = contato[2]
                endereco = contato[3]
                incluir_editar_contato(nome,tel, email, endereco)
            print('>>>> Agenda importada com sucesso!')
    except Exception as e:
        print('>>>> Algum erro ocorreu', e)

def load():
    nome_do_arquivo = 'database.csv'
    try:
        with open(nome_do_arquivo, 'r') as file:
            imports = file.readlines()
            for linha in imports:
                contato = linha.strip().split(',')
                nome = contato[0]
                tel = contato[1]
                email = contato[2]
                endereco = contato[3]

                AGENDA[nome] = {
                    'tel': tel,
                    'email': email,
                    'endereco': endereco
                }

            print('>>>> Agenda carregada com sucesso!')
            print('>>>> Foi carregado {} contatos!'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as e:
        print('>>>> Algum erro ocorreu', e)

def menu_do_usuario():
    print("-----------------------------------------------")
    print('1- Mostrar Contatos')
    print('2- Buscar Contato')
    print('3- Incluir Contato')
    print('4- Editar Contato')
    print('5- Excluir Contato')
    print('6- Exportar agenda em CSV')
    print('7- Importar agenda CSV')
    print('0- Sair')
    print("-----------------------------------------------")

load()
while True:
    menu_do_usuario()
    opcao = input('Digite uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        try:
            contato = input('Nome do contato: ')
            tel, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, tel, email, endereco)
            print('>>>> Contato {} adicionado com sucesso!'.format(contato))
        except Exception as error:
            print('>>>> Um erro inesperado aconteceu!')
    elif opcao == '4':
        contato = input('Nome do contato: ')
        try:
            AGENDA[contato]
            tel, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, tel, email, endereco)
            print('>>>> Contato {} editado com sucesso!'.format(contato))
        except KeyError:
            print('>>>> Esse contato não existe')
        except Exception as error:
            print('>>>> Um erro inesperado aconteceu')
    elif opcao == '5':
        contato = input('Nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '7':
        file = input('Digite o nome do arquivo: ')
        importar_contatos(file)
    elif opcao == '0':
        print('Programa finalizadao!')
        break
    else:
        print('Opção inválida, digite novamente')
        opcao = input('Digite uma opção: ')






