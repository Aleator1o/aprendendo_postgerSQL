nesta brench, eu passei novamente o mesmo arquivo, porém com o arquivo obtendo uma nova tabela chamada 'comentarios', aonde eu pratiquei a utilização dos comandos REFERENCES para tornar uma coluna em uma chave estrangeira, utilizei o JOIN para selecionar mais de uma tabela e mostrar quais comentários foram feitos pelo um usuário específico através da coluna estrangeira, e entendi a diferença na hora de usar o WHERE e o ON. Vou por aqui em baixo os comando usado, mesmo, não sendo necessário, mas para facilitar o acesso aos comandos usado.

INSERT INTO comentarios(id_comentario, id_usuario, titulo, comentario)
VALUES (1, 2, 'minha primeira vez neste site', 'Olá está é a minha primeira conta neste site, e gosto muito desta comunidade, pois todos se ajudam e tiram duvidas entre si, aonde o mais experiente ajuda a solucionar as duvidas, as vezes tem um pouco de comflito quando duas pessoas experientes tentam ajudar, porem a forma de ajuda e completamente distinta, mas o resultado ainda é a mesma');

SELECT comentarios.id_usuario, comentarios.titulo, comentarios.comentario, usuarios.id_usuario
FROM comentarios
JOIN usuarios ON comentarios.id_usuario = usuarios.id_usuario;

Na verdade, depois disso eu fui usar o JOIN e o WHERE na mesma situações e em situações distintas, e vi que o resultado é o mesmo, então ao invés de usar o SELECT que foi usado em cima eu também posso usar da seguinte maneira, que vai dar o mesmo resultado.

SELECT comentarios.id_usuario, comentarios.titulo, comentarios.comentario, usuarios.id_usuario
FROM comentarios, usuarios
WHERE comentarios.id_usuario = usuarios.id_usuario;

E também entendi que o SELECT vai mostrar tudo o que estiver lá e na ordem que estiver, então só é necessário por no SELECT aquilo que você quer que seja mostrado, e na ordem que você queira que seja mostrado, então quando eu fiz o teste do JOIN e do WHERE, eu mudei a ordem e troquei uma coluna, e removi uma que não era necessário, ficando assim.

SELECT comentarios.nome_usuario, comentarios.titulo, comentarios.comentario
FROM comentarios, usuarios
WHERE comentarios.id_usuario = usuarios.id_usuario;
