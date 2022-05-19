insert into Usuario  values(2, 'Maria', 'https://imgur.com/gallery/6bRnrbq', '2022-03-20 17:29:00', 'maria123', 0, 0, 'Bronze', 23);
insert into Usuario  values(1, 'João', 'https://i.imgur.com/HgGuslR.png', '2022-02-17 00:00:01', 'joao456', 10, 20, 'Ouro', 15);
insert into Usuario  values(5, 'José', 'https://i.imgur.com/az3Of6H.jpeg', '2022-03-23 20:00:00', 'jose_789', 5, 10, 'Prata', 56);
insert into Usuario  values(7, 'Alfredo', 'https://i.imgur.com/Ai17gyP.jpeg', '2022-03-31 09:33:00', 'alfredo', 10, 15, 'Bronze', 18);
insert into Usuario  values(10, 'Melissa', 'https://i.imgur.com/epf65jf.png', '2022-04-17 22:15:00', 'mel_10', 0, 0, 'Bronze', 10);

insert into Idioma  values('Inglês');
insert into Idioma  values('Espanhol');
insert into Idioma  values('Francês');
insert into Idioma  values('Alemão');
insert into Idioma  values('Italiano');
insert into Idioma  values('Finlandês');
insert into Idioma  values('Japonês');
insert into Idioma  values('Chinês');
insert into Idioma  values('Russo');

insert into Licao  values(1, 'Hello World!', 5, 'Bem-vindo ao curso de Inglês do Triolingo!', 'Escreva a seguinte palavra em inglês: Cachorro, Escreva a seguinte palavra em inglês: Carro', 1, true, 'Inglês');
insert into Licao  values(10, 'Concordância Verbal', 5, 'O verbo concorda em número e pessoa com o sujeito da frase. Elle travaillait à Paris.', 'Traduza a seguinte frase em francês: Mes chiens sont jolies, Escreva a seguinte frase em francês: Meu carro é verde', 3, true, 'Francês');
insert into Licao  values(7, 'Planos', 5, 'Você fala sobre seus planos com Going To', 'Traduza a seguinte frase em inglês: We are going to study tomorrow, Qual destas palavras significa "Prédio": Building Apartment House Cheese', 2, true, 'Inglês');
insert into Licao  values(36, 'Expressões', 10, 'Vamos aprender algumas expressões idiomáticas em inglês!', 'Traduza a seguinte frase em inglês: It''s raining cats and dogs!, Traduza a seguinte frase em inglês: The pen is mightier than the sword.', 0, false, 'Inglês');
insert into Licao values(72, 'Tipos de Queijo', 5, 'Vamos aprender um pouco mais sobre a cultura gastronômica da França!', 'Escreva a seguinte palavra em francês: Queijo', 0, false, 'Francês');
insert into Licao values(23, 'Piadas', 7, 'Aprenda piadas para socializar com amigos de fala inglesa', 'Traduza a seguinte frase do inglês: Why did the chicken cross the road?', 0, false, 'Inglês');

insert into Login  values('maria@email.com', true, 'senha123', 2);
insert into Login  values('jose@email.com', true, 'senha456', 5);
insert into Login  values('joao@email.com', true, 'senha789', 1);
insert into Login  values('alfredo@email.com', true, 'senha101112', 7);
insert into Login  values('melissa@email.com', false, '123456', 10);

insert into Meta_diaria  values(50, '2022-03-31 16:25:00', 5, 20, true, 2);
insert into Meta_diaria  values(75, '2022-04-01 10:06:00', 5, 40, false, 2);
insert into Meta_diaria  values(30, '2022-03-20 17:29:00', 5, 10, true, 7);
insert into Meta_diaria  values(80, '2022-04-17 22:16:00', 5, 10, false, 10);

insert into Thread values(168, 'Acabei de completar o curso de francês!', 'Francês');
insert into Thread values(250, 'Alguém mais tendo dificuldade com essa questão?', 'Inglês');
insert into Thread values(87, 'Alguns conselhos no inglês?', 'Inglês');

insert into Comentario values(107, 'Acabei de completar o curso de francês!', false, 2, 168);
insert into Comentario values(108, 'Parabéns!', false, 5, 168);
insert into Comentario values(200, 'Alguém mais tendo dificuldade com essa questão?', false, 1, 250);
insert into Comentario values(305, 'Alguém para me ajudar com meu estudo do inglês? Preciso de ajuda!', false, 7, 87);
insert into Comentario values(306, 'Oi! Poderia me passar seu contato?', false, 5, 87);
insert into Comentario values(307, 'Claro, é alfredo@email.com', false, 7, 87);

insert into Licao_Nova values('Expressões', 36);
insert into Licao_Nova values('Tipos de queijo', 72);
insert into Licao_Nova values('Piadas', 23);

insert into Conquista values('Prata', 'Coruja esperta');
insert into Conquista values('Ouro', 'Coruja super-heroi');
insert into Conquista values('Bronze', 'Coruja detetive');

insert into Produto values(1025, '2022-04-20 15:15:00', 30, null, 'Tipos de queijo');
insert into Produto values(240, '2022-03-01 14:00:00', 20, 'Bronze', null);
insert into Produto values(300, '2022-04-05 08:30:00', 30, null, 'Expressões');

insert into Podcast values(2056, 'Inglês Para Iniciantes', 'Inglês');
insert into Podcast values(3000, 'Falando Francês como um Nativo', 'Francês');
insert into Podcast values(1072, 'Hello There', 'Inglês');

insert into Audio values('Episódio 14: Emergency Landing', '00:25:41', 'https://podcast.duolingo.com/episodio-14-emergency-landings-pousos-forcados-pt.html', 1072);
insert into Audio values('Episódio 64: A Chocolateria', '00:23:27', 'https://podcast.duolingo.com/episode-64-la-chocolatiere-the-chocolate-maker', 3000);
insert into Audio values('Episódio 9: Animais Selvagens', '00:24:10', 'https://podcast.duolingo.com/episodio-9-wild-animals-animais-selvagens-pt.html', 2056);

insert into Estudo values(5, 2, 'Francês');
insert into Estudo values(1, 7, 'Inglês');
insert into Estudo values(3, 5, 'Inglês');
insert into Estudo values(2, 1, 'Francês');
insert into Estudo values(1, 1, 'Inglês');

insert into Seguir values(5, 7);
insert into Seguir values(7, 5);
insert into Seguir values(2, 1);
insert into Seguir values(2, 7);

insert into Compra values(5, 1025);
insert into Compra values(2, 240);
insert into Compra values(1, 300);

insert into Ouve values(1, 3000);
insert into Ouve values(2, 3000);
insert into Ouve values(5, 1072);
insert into Ouve values(5, 2056);
insert into Ouve values(7, 2056);

insert into Acessa values(7, 1, false);
insert into Acessa values(2, 10, true);
insert into Acessa values(5, 10, false);
insert into Acessa values(1, 1, true);
insert into Acessa values(1, 7, true);

insert into Antecede values(107, 108);
insert into Antecede values(305, 306);
insert into Antecede values(306, 307);