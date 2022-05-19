# Imprimir resultados na tela

from tabulate import tabulate

def printResults(description, results):
    headers = []
    for tab in description:
        headers.append(tab[0])
    
    print("\n"+tabulate(results, headers))
    if len(results)==0:
        print("A consulta não retornou nenhum valor.")
    return

# Todas as funções precisam do cursor

# Funções para View
def createViewMetasCumpridas (cursor, data_intervalo):
    metascumpridas = """create view MetasCumpridas as
                        select usuario_id as cumpriu_meta from Meta_diaria
                        where completa = true and metadiaria_data::timestamp::date between (%s) and (current_date);"""
    cursor.execute(metascumpridas, [data_intervalo])
    return
def dropViewMetasCumpridas (cursor):
    dropmetascumpridas = """drop view MetasCumpridas;"""
    cursor.execute(dropmetascumpridas)
    return

# Todas as queries retornam resultados

# Todos os idiomas em que o usuário não está inscrito, mas que seus amigos estão
def queryIdiomasAmigos (cursor, usuario_id):
    query = """select distinct idioma_nome
               from Seguir join Usuario on (Seguir.seguido = Usuario.usuario_id) join Estudo using (usuario_id)
               where segue=(%s)
               intersect
               select distinct idioma from Idioma left join Estudo E on (Idioma.idioma = E.idioma_nome)
               where not exists (select idioma_nome from Estudo
				                 where usuario_id=(%s) and
				                 idioma_nome in (select distinct idioma_nome
								                from Estudo where usuario_id = E.usuario_id));"""
    cursor.execute(query, [usuario_id, usuario_id])
    results = cursor.fetchall()
    return (cursor.description, results)

# Todos os usuários que não cumpriram a meta diária e também não fizeram nenhuma lição no intervalo
# MetasCumpridas precisa ser dropada e criada antes de fazer o query, porque depende dela
def queryAusentePeriodo (cursor, data_intervalo):
    dropViewMetasCumpridas(cursor)
    createViewMetasCumpridas(cursor, data_intervalo)
    query = """select usuario_id from Usuario
               where usuario_id not in (select * from MetasCumpridas)
               intersect
               select usuario_id from Usuario
               where usuario_id not in (select usuario_id from Usuario join Acessa using (usuario_id)
				                		 where data_acesso::timestamp::date between (%s)
                                         and current_date);"""
    cursor.execute(query, [data_intervalo])
    results = cursor.fetchall()
    return (cursor.description, results)

# Lista todos os usuários de um idioma que ainda não seguem o usuário repassado
def queryNaoSeguem (cursor, id, idioma):
    query = """select nome, usuario_id from usuario
               where usuario_id not in (select segue from Seguir where seguido=(%s))
               and usuario_id IN (select usuario_id from estudo where idioma_nome=(%s));"""
    cursor.execute(query, [id, idioma])
    results = cursor.fetchall()
    return (cursor.description, results)

# Retorna o nome e o xp dos usuários de um idioma que cumpriram a meta diária de um intervalo
def queryUsuariosMetaDiaria (cursor, idioma, data_intervalo):
    dropViewMetasCumpridas(cursor)
    createViewMetasCumpridas(cursor, data_intervalo)
    query = """select nome as nome_usuario, xp from usuario
               where usuario_id in (select usuario_id from estudo
                                   	where usuario_id in (select cumpriu_meta from MetasCumpridas)
                                   	and idioma_nome=(%s));"""
    cursor.execute(query, [idioma])
    results = cursor.fetchall()
    return (cursor.description, results)

# Pesquisa todos os usuários não verificados e que cumpriram metas em um intervalo
def queryNaoVerificados(cursor, data_intervalo):
    dropViewMetasCumpridas(cursor)
    createViewMetasCumpridas(cursor, data_intervalo)
    query = """select Usuario.nome as nome_usuario from Usuario join Login using (usuario_id)
               where usuario_id in (select cumpriu_meta from MetasCumpridas)
               and verificado=false;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return (cursor.description, results)

# Lista todos os podcasts de todos os idiomas, quantos áudios cada um tem e quantas pessoas os ouvem
def queryPodcastsEstatisticas (cursor):
    query = """select idioma, nome as nome_podcast, t1.num_audios, t2.num_ouvintes
               from (select idioma, Podcast.nome, count (*) as num_audios
                     from Audio join Podcast using (podcast_id)
                     group by Podcast.nome, idioma
                     order by idioma) t1
               join (select nome, count (*) as num_ouvintes
                     from Podcast join Ouve using (podcast_id)
                     group by Podcast.nome) t2
               using (nome);"""
    cursor.execute(query)
    results = cursor.fetchall()
    return (cursor.description, results)

# Lista todos os podcasts de todos os idiomas que um usuário repassado estuda
def queryPodcastsUsuario(cursor, id):
    query = """select Usuario.nome, idioma, Podcast.nome as nome_podcast
               from Usuario join Estudo using (usuario_id) join Podcast on (Estudo.idioma_nome = Podcast.idioma)
               where usuario_id = (%s)
               order by idioma;"""
    cursor.execute(query, [id])
    results = cursor.fetchall()
    return (cursor.description, results)

# Todos as compras na plataforma em um intervalo e quais foram os produtos
def queryCompras(cursor, data_intervalo):
    dropViewMetasCumpridas(cursor)
    createViewMetasCumpridas(cursor, data_intervalo)
    query = """select usuario_id, 'Conquista' as produto
               from Compra join Produto using (produto_id) join Conquista
                        on (Produto.conquista_id = Conquista.classe)
               where conquista_id is not null and produto_data::timestamp::date between (%s) and current_date
               union
               select usuario_id, 'Lição Nova' as produto
               from Compra join Produto using (produto_id) join Licao_Nova
                        on (Produto.licao_nova_id = Licao_Nova.titulo)
               where licao_nova_id is not null and produto_data::timestamp::date between (%s) and current_date;"""
    cursor.execute(query, [data_intervalo, data_intervalo])
    results = cursor.fetchall()
    return (cursor.description, results)

# Lista todas as conquistas compradas por usuário e suas descrições em um dado intervalo de tempo
def queryConquistasCompradas(cursor, data_intervalo):
    query = """select usuario_id, descricao as conquista
               from Compra join Produto using (produto_id) join Conquista
                        on (Produto.conquista_id = Conquista.classe)
               where conquista_id is not null and produto_data::timestamp::date between
                                                    (%s) and current_date;"""
    headers = []
    cursor.execute(query, [data_intervalo])
    
    
    
    results = cursor.fetchall()
    return (cursor.description, results)

# Lista todas as lições liberadas para um usuário repassado e completadas em um idioma repassado
def queryLicoesDesbloqueadas(cursor, id, idioma):
    query = """select nome, completa from Licao join Acessa using (licao_id)
               where usuario_id=(%s) and nivel <= (select nivelamento from estudo
                                                    where usuario_id=(%s) and idioma=(%s));"""
    cursor.execute(query, [id, id, idioma])
    results = cursor.fetchall()
    return (cursor.description, results)

# Pesquisa o número de usuários, a média de lições obrigatórias completadas, quantas threads existem,
# quantos comentários foram postados e quantas pessoas ouvem podcasts para cada idioma
def queryIdiomaEstatisticas (cursor):
    query = """select idioma, num_usuarios, med_lic_obrig_complet, num_threads, num_comentarios, num_ouvintes_podcasts
               from	(select idioma, num_usuarios, cast(cast((cast(t2.num_licoes as float) / cast(t1.num_usuarios as float))
							as decimal(5,2)) as float) as med_lic_obrig_complet
               from (select idioma_nome as idioma, count(*) as num_usuarios from Estudo
	  	       group by idioma_nome) t1
	           join (select idioma, count (*) as num_licoes
			   from Acessa join Licao using (licao_id)
			   where completa=true and obrigatoria=true
			   group by idioma) t2
	           using (idioma)) Q1
               join (select idioma, count (*) as num_threads
                     from Thread
                     group by idioma) Q2 using (idioma)
               join (select idioma, cast(sum(C1.num_comentarios) as int) as num_comentarios
               from (select idioma, Thread.nome, count (*) as num_comentarios
               from Thread join Comentario using (thread_id) group by thread_id) C1
               group by idioma) Q3 using (idioma)
               join (select idioma, count (*) as num_ouvintes_podcasts
                     from Ouve join Podcast using (podcast_id)
                     group by idioma) Q4 using (idioma);"""
    cursor.execute(query)
    results = cursor.fetchall()
    return (cursor.description, results)