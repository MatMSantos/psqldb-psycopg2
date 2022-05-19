from venv import create
import psycopg2

from functions import *

# Mateus Moreira Santos - 00243714
# Jonathan Gabriel Nunes Mendes - 00290195

try:
    connection = psycopg2.connect(user="postgres",
                                  password=";Wj[QhL~4E0XeXrM",
                                  host="localhost",
                                  port="5432",
                                  database="TriolingoDB")
    print("-- Conexão bem sucedida.")

except (Exception, psycopg2.Error) as error:
    print("-- Failed to connect to database", error)

cursor = connection.cursor()

print("""
=== Banco de Dados TRIOLINGO ===

Escolha qual pesquisa realizar:

1. Todos os idiomas em que um usuário repassado não está inscrito, mas que seus amigos estão
2. Todos os usuários que não cumpriram a meta diária e também não fizeram nenhuma lição no intervalo
3. Lista todos os usuários de um idioma que ainda não seguem o usuário repassado
4. Retorna o nome e o xp dos usuários de um idioma que cumpriram metas diárias em um intervalo
5. Pesquisa todos os usuários não verificados e que cumpriram metas em um intervalo
6. Lista todos os podcasts de todos os idiomas, quantos áudios cada um tem e quantas pessoas os ouvem
7. Lista todos os podcasts de todos os idiomas que um usuário repassado estuda
8. Todos as compras na plataforma em um intervalo e quais foram os produtos
9. Lista todas as conquistas compradas pelos usuários e suas descrições
10. Lista todas as lições liberadas para um usuário repassado e completadas em um idioma repassado
11. Pesquisa o número de usuários, a média de lições obrigatórias completadas, quantas threads existem,
    quantos comentários foram postados e quantas pessoas ouvem podcasts para cada idioma

ou digite "Exit" para sair.
""")

while(1):
    print("\nDigite sua opção:")
    main_input = input()
    exit_flag = False

    if(main_input == "1"):
        print("Qual o id do usuário que você quer buscar? ")
        id = input()

        try:
            description, results = queryIdiomasAmigos(cursor, id)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "2"):
        print("Qual a data para pesquisar? ")
        intervalo = input()

        try:
            description, results = queryAusentePeriodo(cursor, intervalo)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "3"):
        print("Qual o id do usuário a ser pesquisado?")
        id = input()
        print("Qual o idioma referido?")
        idioma = input()

        try:
            description, results = queryNaoSeguem(cursor, id, idioma)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "4"):
        print("Qual o idioma referido?")
        idioma = input()
        print("Qual a data para pesquisar? ")
        intervalo = input()

        try:
            description, results = queryUsuariosMetaDiaria(cursor, idioma, intervalo)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "5"):
        try:
            print("Qual a data para pesquisar? ")
            intervalo = input()
            description, results = queryNaoVerificados(cursor, intervalo)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "6"):
        try:
            description, results = queryPodcastsEstatisticas(cursor)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "7"):
        print("Qual o id do usuário a ser pesquisado?")
        id = input()

        try:
            description, results = queryPodcastsUsuario(cursor, id)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "8"):
        print("Qual a data para pesquisar? ")
        intervalo = input()

        try:
            description, results = queryCompras(cursor, intervalo)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "9"):
        print("Qual a data para pesquisar? ")
        intervalo = input()

        try:
            description, results = queryConquistasCompradas(cursor, intervalo)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "10"):
        print("Qual o id do usuário a ser pesquisado?")
        id = input()
        print("Qual o idioma referido?")
        idioma = input()

        try:
            description, results = queryLicoesDesbloqueadas(cursor, id, idioma)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "11"):
        try:
            description, results = queryIdiomaEstatisticas(cursor)
            printResults(description, results)
        except (Exception, psycopg2.Error) as error:
            print("-- Failed to execute query")
    elif(main_input == "Exit" or main_input == "exit"):
        break
    else:
        print("Não é uma oção válida. Digite novamente:")
        continue

    while(1):
        print("\nVocê deseja fazer uma nova consulta? (s/n)")
        repeat = input()
        if(repeat == "s" or repeat == "S"):
            break
        elif(repeat == "n" or repeat == "N"):
            exit_flag = True
            break
        else:
            print("Não é uma oção válida. Digite novamente:")  
    
    if(exit_flag): break
    else: continue

print("\n-- Encerrando o programa. . .")

print("\nVocê quer que as alterações no banco de dados sejam salvas? (s/n)")
while(1):
        repeat = input()
        if(repeat == "s" or repeat == "S"):
            # Tornar edições permanentes
            connection.commit()
            print("Salvando alterações. . .")
            break
        elif(repeat == "n" or repeat == "N"):
            print("Alterações ignoradas.")
            break
        else:
            print("Não é uma oção válida. Digite novamente:")


# closing database connection.
if connection:
    cursor.close()
    connection.close()
    print("-- PostgreSQL connection is closed")