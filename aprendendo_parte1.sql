SELECT usuarios.nome_usuario, comentarios.titulo, comentarios.comentario
FROM comentarios, usuarios
WHERE comentarios.id_usuario = 1 AND usuarios.id_usuario = 1;