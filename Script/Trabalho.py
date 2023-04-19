import sqlite3 as banco
import os
import time

def preencher_tabelas():
    with open('Database/Nomes.txt', 'r') as arquivo:
            for frase in arquivo:
                
            
                palavra = frase.split()
            
                palavra1 = palavra[0]
                palavra2 = palavra[1]
                palavra3 = palavra[2]
                palavra4 = palavra[3]
                palavra5 = palavra[4]
                palavra6 = palavra[5]

            
                cursor.execute(f"""INSERT INTO pessoa(cpf, primeiro_nome, nome_do_meio, sobrenome, Idade, conta) VALUES ('{palavra1}', '{palavra2}', '{palavra3}', '{palavra4}', '{palavra5}', '{palavra6}')""")
                conexão.commit()

            arquivo.close()
    with open('Database/Contas.txt', 'r') as file:
            for frase in file:
                
            
                palavra = frase.split()
            
                palavra1 = palavra[0]
                palavra2 = palavra[1]
                palavra3 = palavra[2]
                palavra4 = palavra[3]
                palavra5 = palavra[4]

            
                cursor.execute(f"""INSERT INTO conta(Agência, Número, Saldo, Gerente, Titular) VALUES ('{palavra1}', '{palavra2}', '{palavra3}', '{palavra4}', '{palavra5}')""")
                conexão.commit()

            arquivo.close()


def escolhas():
    os.system('cls')
    print('\n\t   -----: Menu :-----')
    print('\n[1] - Para inserir novos dados nas tabelas.')
    print('[2] - Para deletar algum dado na tabela.')
    print('[3] - Para alterar algum dado na tabela.')
    print('[4] - Para fazer consulta.')
    print('[5] - Sair')
    opcao = input('> Escolha uma das opções acima: ')
    if opcao == '1':
        inserir_dados()
    elif opcao == '2':
        deletar_dados()
    elif opcao == '3':
        atualizar_dados()
    elif opcao == '4':
        consulta_save()
    elif opcao == '5':
        print('-- Saindo, até logo!')
    elif opcao != '1':
        os.system('cls')
        print('\n[-] Valor inserido inválido! Tente novamente.\n')
        escolhas()


def consulta():
    cursor.execute(f"""SELECT * FROM pessoa""")
    consultaF = cursor.fetchall()
    for frase in consultaF:
        print('Cliente: {}' .format(frase))

    cursor.execute(f"""SELECT * FROM conta""")
    consultaD = cursor.fetchall()
    for frase1 in consultaD:
        print('Contas: {}' .format(frase1))


def consulta_save():
    os.system('cls')
    print('\t- SELECIONADO: CONSULTAR DADOS -')
    print('\n>> Tabelas disponíveis para consulta:')
    print('[1] - Pessoa')
    print('[2] - Conta')
    desc = input('\n> Em qual tabela deseja fazer a consulta ?: ')
    if desc == 'Pessoa' or desc =='pessoa' or desc == '1':
        print('[1] - CPF')
        print('[2] - Primeiro Nome')
        print('[3] - Nome do Meio')
        print('[4] - sobrenome')
        print('[5] - Idade')
        print('[6] - conta')
        escol_colum = input('Quais das opções acima deseja consultar ?: ')  
        if escol_colum == 'CPF' or escol_colum == 'cpf' or escol_colum == '1':
            cursor.execute(f"""SELECT id,cpf FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('\n> Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT cpf FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('CPF'):
                os.makedirs('CPF')
            arquivoSav = open('CPF/SavCpf.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - CPF:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))
            
        elif escol_colum == 'Primeiro Nome' or escol_colum == 'primeiro nome' or escol_colum == '2':
            cursor.execute(f"""SELECT id,primeiro_nome FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('\n> Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT primeiro_nome FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Primeiro Nome'):
                os.makedirs('Primeiro Nome')
            arquivoSav = open('Primeiro Nome/Savprimeiro_nome.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Primeiro Nome:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum == 'Nome Do Meio' or escol_colum == 'nome do meio' or escol_colum == '3':
            cursor.execute(f"""SELECT id,nome_do_meio FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT nome_do_meio FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Nome Do Meio'):
                os.makedirs('Nome Do Meio')
            arquivoSav = open('Nome Do Meio/SavNome_meio.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Nome Do Meio:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum == 'Sobrenome' or escol_colum == 'sobrenome' or escol_colum == '4':
            cursor.execute(f"""SELECT id,sobrenome FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('\n> Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT sobrenome FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Sobrenome'):
                os.makedirs('Sobrenome')
            arquivoSav = open('Sobrenome/SavSobrenome.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Sobrenome:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum == 'Idade' or escol_colum == 'idade' or escol_colum == '5':
            cursor.execute(f"""SELECT id,Idade FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Idade FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Idade'):
                os.makedirs('Idade')
            arquivoSav = open('Idade/SavIdade.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Idade:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum == 'Conta' or escol_colum == 'conta' or escol_colum == '6':
            cursor.execute(f"""SELECT id,conta FROM pessoa""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT conta FROM pessoa WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Conta'):
                os.makedirs('Conta')
            arquivoSav = open('Conta/SavConta.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Conta:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

    elif desc =='Conta' or desc =='conta' or desc =='2':
        print('[1] - Agência')
        print('[2] - Número')
        print('[3] - Saldo')
        print('[4] - Gerente')
        print('[5] - Titular')
        escol_colum = input('\n> Quais das opções acima deseja consultar ?: ') 

        if  escol_colum == 'Agencia' or escol_colum == 'agencia' or escol_colum == '1':
            cursor.execute(f"""SELECT id,Agência FROM conta""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('\n> Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Agência FROM conta WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Agência'):
                os.makedirs('Agência')
            arquivoSav = open('Agência/SavAgência.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Agência:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))
            
        elif escol_colum =='Numero' or escol_colum =='numero' or escol_colum =='2':
            cursor.execute(f"""SELECT id,Número FROM conta""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Número FROM conta WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Número'):
                os.makedirs('Número')
            arquivoSav = open('Número/SavNúmero.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Número:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum =='Saldo' or escol_colum =='saldo' or escol_colum =='3':
            cursor.execute(f"""SELECT id,Saldo FROM conta""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Saldo FROM conta WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Saldo'):
                os.makedirs('Saldo')
            arquivoSav = open('Saldo/SavSaldo.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Saldo:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum =='Gerente' or escol_colum =='gerente' or escol_colum =='4':
            cursor.execute(f"""SELECT id,Gerente FROM conta""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Gerente FROM conta WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Gerente'):
                os.makedirs('Gerente')
            arquivoSav = open('Gerente/SavGerente.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Gerente:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))

        elif escol_colum =='Titular' or escol_colum =='titular' or escol_colum =='5':
            cursor.execute(f"""SELECT id,Titular FROM conta""")
            save = cursor.fetchall()
            for linhas in save:
                print('- Resultado da consulta: {}' .format(linhas))
            id_escol = input('Digite o id do cliente que deseja salvar a consulta: ')
            cursor.execute(f"""SELECT Titular FROM conta WHERE id='{id_escol}'""")
            cons_sav = cursor.fetchone()
            cons_sav = str(cons_sav)
            if not os.path.exists('Titular'):
                os.makedirs('Titular')
            arquivoSav = open('Titular/SavTitular.txt', 'a')
            arquivoSav.write(f'\nid:{id_escol} - Titular:{cons_sav}')
            arquivoSav.close()
            print('\n[+] Consulta Salva: {}' .format(cons_sav))
    else:
        print('\n[-] Opção inválida!')
        time.sleep(0.8)
        consulta_save()

    retorn = input('>> Deseja fazer mais alguma consulta (y/n)?: ')
    if retorn =='y':
        consulta_save()
    else:
        print('[+] Consultas Finalizadas! Voltando ao menu...')
        time.sleep(2)
        escolhas()

def inserir_dados():
    os.system('cls')
    print('\t- SELECIONADO: INSERIR DADOS - \n>> Insira os seguintes dados: ')
    CPF = input('\n> CPF: ')
    nome = input('> Primeiro nome: ')
    nome_meio = input('> Nome do meio: ')
    sobrenome = input('> Sobrenome: ')
    idade = input('> Idade: ')
    conta = input('> Conta: ')
    nome_meioF = bool(nome_meio)
    if nome_meioF == 0:
        nome_meioF = 'Vazio'
    else:
        nome_meioF = nome_meio
    
    cursor.execute(f"""INSERT INTO pessoa(cpf, primeiro_nome, nome_do_meio, sobrenome, Idade, conta) VALUES('{CPF}', '{nome}', '{nome_meioF}', '{sobrenome}', '{idade}', '{conta}')""")
    conexão.commit()

    agencia = input('> Agência: ')
    numero = input('> Numero: ')
    saldo = input('> Saldo: ')
    gerente = input('> Numeração do gerente: ')

    cursor.execute(f"""INSERT INTO conta(Agência, Número, Saldo, Gerente, Titular) VALUES('{agencia}', '{numero}', '{saldo}', '{gerente}', '{conta}')""")
    conexão.commit()
    print('\n[+] Dados inseridos com êxito!')
    time.sleep(2)
    escolhas()

def deletar_dados():
    consulta()
    print('\n[~] DESCRIÇÃO: ID, AGÊNCIA, NUMERO, SALDO, GERENTE, TITULAR')
    print('\n\t- SELECIONADO: DELETAR DADOS - ')
    con_delete = int(input('\n> Digite a ID do Cliente a ser deletado: '))
    cursor.execute(f"""DELETE FROM pessoa WHERE id='{con_delete}'""")
    cursor.execute(f"""DELETE FROM conta WHERE id='{con_delete}'""")
    conexão.commit()
    print('\n[+] Cliente com ID {} foi deletado com êxito!' .format(con_delete))
    time.sleep(2)
    escolhas()


def atualizar_dados():
    consulta()
    print('\n\t- SELECIONADO: ATUALIZAR DADOS -\n')
    print('[1] Nome\n[2] Nome do meio\n[3] Sobrenome\n[4] CPF\n[5] Idade\n[6] Conta')
    alterar_tab = input('> Escolha uma das opções acima para alteração: ')
    if alterar_tab == 'Nome' or alterar_tab == 'nome' or alterar_tab == '1':
        print('\n\t- SELECIONADO: Nome -\n')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET primeiro_nome='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    elif alterar_tab == 'Nome do meio' or alterar_tab == 'nome do meio' or alterar_tab == '2':
        print('\n\t- SELECIONADO: Nome do meio -\n')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET nome_do_meio='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    elif alterar_tab == 'Sobrenome' or alterar_tab == 'sobrenome' or alterar_tab == '3':
        print('\n\t- SELECIONADO: Sobrenome -\n')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET sobrenome='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    elif alterar_tab == 'CPF' or alterar_tab == 'cpf' or alterar_tab =='4':
        print('\n\t- SELECIONADO: CPF -\n')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET cpf='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    elif alterar_tab == 'Idade' or alterar_tab == 'idade' or alterar_tab =='5':
        print('\n\t- SELECIONADO: Idade -\n')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET idade='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    elif alterar_tab == 'Conta' or alterar_tab == 'conta' or alterar_tab == '6':
        print('\n\t- SELECIONADO: Conta -')
        val_antigo = input('> Digite o id do cliente: ')
        alteracao = input("> Digite sua alteração: ")
        cursor.execute(f"""UPDATE pessoa SET conta='{alteracao}' WHERE id='{val_antigo}'""")
        conexão.commit()
        print('\n[+] Os dados foram atualizados!')
    else:
        print('\n[-] Opção inválida!')
        time.sleep(2)
        atualizar_dados()

    des = input('\n>> Deseja continuar fazendo alterações (y/n)?')
    if des == 'y':
        atualizar_dados()
    else:
        print('>> Okay! Voltando ao menu principal...')
        time.sleep(2)
        escolhas()
try:

    
    conexão = banco.connect('Database/Banco.db')
    os.system('cls')
    print('[*] Conectando-se ao banco de dados...')
    time.sleep(3)
    cursor = conexão.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pessoa';")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='conta';")
    table_exist = bool(cursor.fetchone())
    if not table_exist:

        print('[~] Banco de dados não existe, criando...')
        time.sleep(5)
        cursor.execute("""CREATE TABLE pessoa(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cpf VARCHAR(11) NOT NULL,
            primeiro_nome TEXT NOT NULL,
            nome_do_meio TEXT,
            sobrenome TEXT,
            Idade INTEGER,
            conta INTEGER,
            FOREIGN KEY(id) REFERENCES conta(id)
        );""")

        cursor.execute("""CREATE TABLE conta(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Agência VARCHAR(10) NOT NULL,
            Número VARCHAR(20),
            Saldo REAL NOT NULL,
            Gerente INTEGER NOT NULL,
            Titular INTEGER NOT NULL
        );""")

        print('\n[+] Banco de dados criado.\n\n')
        time.sleep(1)
        print('[~] Inserindo informações já registradas....')
        preencher_tabelas()
        print('\n\t[+] Banco de dados preenchido!')
        opcao_esc = input('>> Deseja fazer alguma alteração no banco?(y/n): ')
        if opcao_esc == 'y':
            time.sleep(1)
            escolhas()
        elif opcao_esc == 'n':
            print('-- Saindo, até logo!')
        else:
            print('\n[-] Opção inválida!\n')
    else:

        cursor.execute('SELECT * FROM pessoa')
        table_preencher = bool(cursor.fetchone())
        if table_preencher == 1:
            print('\n\t[+] Banco de dados preenchido!')
            opcao_esc = input('>> Deseja fazer alguma alteração no banco?(y/n): ')
            if opcao_esc == 'y':
                time.sleep(1)
                escolhas()
            elif opcao_esc == 'n':
                print('-- Saindo, até logo!')
            else:
                print('\n[-] Opção inválida!\n')

except Exception as error:
    print('Ocorreu erro de: {}' .format(error))
finally:
    if conexão:
        conexão.close
        print('\n>> Conexão Encerrada')