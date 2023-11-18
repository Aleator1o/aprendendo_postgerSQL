INSERT INTO comentarios(id_comentario, id_usuario, titulo, comentario)
VALUES (1, 2, 'minha primeira vez neste site', 'Olá está é a minha primeira conta neste site, e gosto muito desta comunidade, pois todos se ajudam e tiram duvidas entre si, aonde o mais experiente ajuda a solucionar as duvidas, as vezes tem um pouco de comflito quando duas pessoas experientes tentam ajudar, porem a forma de ajuda e completamente distinta, mas o resultado ainda é a mesma');

SELECT comentarios.id_usuario, comentarios.titulo, comentarios.comentario, usuarios.id_usuario
FROM comentarios
JOIN usuarios ON comentarios.id_usuario = usuarios.id_usuario;