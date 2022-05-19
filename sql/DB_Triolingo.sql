drop table if exists Usuario;
drop table if exists Idioma;
drop table if exists Licao;
drop table if exists Login;
drop table if exists Meta_diaria;
drop table if exists Thread;
drop table if exists Comentario;
drop table if exists Produto;
drop table if exists Licao_Nova;
drop table if exists Conquista;
drop table if exists Podcast;
drop table if exists Audio;

-- ENTIDADES
create table Usuario
(usuario_id	int not null,
 nome 	varchar(32) not null,
 foto 	varchar(64),
 usuario_data TIMESTAMP check (usuario_data > '2022-02-17 00:00:00') not null,
 nick varchar(32) not null,
 tringots int check (tringots >= 0) not null,
 xp int check (xp >= 0) not null,
 usuario_rank varchar(10) not null,
 idade smallint check (idade >=0) not null, 
 primary key (usuario_id));

create table Idioma
(idioma varchar(15) not null,
 primary key(idioma));

create table Licao
(licao_id int not null,
 nome varchar(50) not null,
 recompensa smallint check (recompensa >= 0) not null,
 dica text not null,
 questao text not null,
 nivel smallint check (nivel >= 0) not null,
 obrigatoria boolean not null,
 idioma varchar(15) not null,
 primary key (licao_id),
 -- Ensinado
 foreign key (idioma) references Idioma(idioma) on delete cascade on update cascade);

create table Login
(email varchar(32) not null,
 verificado boolean,
 senha varchar(20) not null,
 usuario_id int not null,
 primary key (email),
 -- Vinculo
 foreign key (usuario_id) references Usuario(usuario_id) on delete cascade on update cascade);

create table Meta_diaria
(metadiaria_id smallint not null,
 metadiaria_data timestamp check (metadiaria_data > '2022-02-17 00:00:00') not null,
 premio smallint check (premio > 0) not null,
 valor smallint check (valor > 0) not null,
 completa boolean not null,
 usuario_id int not null,
 primary key (metadiaria_id),
 -- Tem
 FOREIGN key (usuario_id) references Usuario(usuario_id) on delete cascade on update cascade);

create table Thread
(thread_id int not null,
 nome text not null,
 idioma varchar(15) not null,
 primary key (thread_id),
 -- Discussão
 foreign key (idioma) REFERENCES Idioma(idioma) on delete cascade on update cascade);

create table Comentario
(comentario_id int not null,
 texto text not null,
 deletado BOOLEAN not null,
 usuario_id int not null,
 thread_id int not null,
 PRIMARY key (comentario_id),
 -- Postagem
 foreign key (usuario_id) references Usuario(usuario_id) on delete cascade on update cascade,
 -- Composicao
 foreign key (thread_id) references Thread(thread_id) on delete cascade on update cascade);
 
create table Licao_Nova
(titulo varchar(20) not null,
 licao_id int not null,
 primary key (titulo),
 -- Desbloqueia
 foreign key (licao_id) references Licao(licao_id) on delete cascade on update cascade);

create table Conquista
(classe varchar(20) not null,
 descricao varchar(50) not null,
 primary key (classe));

create table Produto
(produto_id int not null,
 produto_data TIMESTAMP check (produto_data > '2022-02-17 00:00:00') not null,
 custo SMALLINT check (custo > 0) not null,
 conquista_id varchar(20),
 licao_nova_id varchar(20),
 primary key (produto_id),
 foreign key (conquista_id) references Conquista(classe)
 	on update cascade on delete cascade,
 foreign key (licao_nova_id) references Licao_Nova(titulo)
	on update cascade on delete cascade);

create table Podcast
(podcast_id int not null,
 nome varchar(50) not null,
 idioma varchar(15) not null,
 primary key (podcast_id),
 -- Pertence
 foreign key (idioma) references Idioma(idioma) on delete cascade on update cascade);

create table Audio
(nome varchar(30) not null,
 duracao time check (duracao > '00:00:00') not null,
 audio_link varchar(100) not null,
 podcast_id int not null,
 primary key (nome),
 -- Publica
 foreign key (podcast_id) references Podcast(podcast_id) on delete cascade on update cascade);

-- RELACIONAMENTOS N-M
create table Estudo
(nivelamento smallint check (nivelamento > 0) not null,
 usuario_id int not null,
 idioma_nome varchar(15) not null,
 foreign key (usuario_id) REFERENCES Usuario(usuario_id) on delete cascade on update cascade,
 foreign key (idioma_nome) REFERENCES Idioma(idioma) on delete cascade on update cascade);

create table Seguir
(segue int not null,
 seguido int not null,
 foreign key (segue) references Usuario(usuario_id) on delete cascade on update cascade,
 foreign key (seguido) references Usuario(usuario_id) on delete cascade on update cascade);

create table Compra
(usuario_id int not null,
 produto_id int not null,
 foreign key (usuario_id) references Usuario(usuario_id) on delete cascade on update cascade,
 foreign key (produto_id) references Produto(produto_id) on delete cascade on update cascade);

create table Ouve
(usuario_id int not null,
 podcast_id int not null,
 foreign key (usuario_id) references Usuario(usuario_id)
 on delete cascade on update cascade,
 foreign key (podcast_id) references Podcast(podcast_id)
 on delete cascade on update cascade);

create table Acessa
(usuario_id int not null,
 licao_id int not null,
 completa BOOLEAN not null,
 foreign key (usuario_id) references Usuario(usuario_id) on delete cascade on update cascade,
 foreign key (licao_id) references Licao(licao_id) on delete cascade on update cascade);
 
create table Antecede
(anterior int not null,
 proximo int not null,
 foreign key (anterior) references Comentario(comentario_id),
 foreign key (proximo) references Comentario(comentario_id));