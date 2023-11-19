Por falta de experiência e pratica, levei bastante tempo pra finalizar, na verdade eu poderia ter finalizado a muito tempo, mas não quis, pois eu queria explorar novas formas de fazer algo, e ate mesmo economizar na criação de funções, mas não consegui se tem uma jeito eu não sei.

Vou resumir o objetivo desta modificação.

O intuito é criar um código, que de forma automática atualizaria para mim os id's dos registro, sem eu ter que ficar fazendo isso de forma manual, este é o objetivo.

Então criei uma função chamada 'criando_novo_id' e este foi o código que eu fiz:

CREATE OR REPLACE FUNTION criando_novo_id() RETURNS TRIGGER AS $$
DECLARE
ultimo_id INT;
BEGIN
SELECT MAX(id_usuario) INTO ultimo_id FROM usuarios;
NEW.id_usuario := ultimo_id + 1;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

Olhando para este código por alguns segundo me toquei que o mesmo só estava funcionando para a tabela 'usuarios', e lembrando da minha experiência com Python, lembrei que uma função tem o intuído de evitar ter que ficar fazendo o mesmo código varias vezes, então comecei a pensar, que eu deveria usar essa mesma função para o gatilho da tabela 'usuarios' e para o gatilho da tabela 'comentarios', e foi ai aonde o meu pesadelo começou.

Por cause de eu ter a ideia de que toda a função deve ser feita para evita repetir comandos, comecei a tentar utilizar o comando 'IF', 'ELSIF' e 'ELSE', para utilizar de valores booleanos para identificar se o NEW.id_usuario era verdadeiro ou não, se fosse verdadeiro o mesmo iria executar o comando para adicionar o novo id no novo registro da tabela usuarios, se não fosse verdadeiro, o mesmo iria executar uma sequencia de comandos para adicionar o novo id no novo registro da tabela comentarios.

Mas eu não esperava que o postgerSQL não iria aceitar isso, então fiquei por mais ou menos duas horas tentado arranjar um jeito de usar uma função em vários trigger's, mas não conseguir, e quando eu já tinha desistido de tudo, lembrei que eu também posso por parâmetros nas funções, que podem ser substituídas quando eu coloco algo que existe. E ainda sim não conseguir fazer uma parâmetro receber uma tabela e por fim consegui a façanha de fazer o paramento não querer aceitar valores inteiros.

Depois de eu ficado por vários minutos tentado fazer isso funcionar a todo custo, eu me rendi, e criei duas funções funções, um para cada trigger fiz os testes e funcionou.

Com todo este trampo, eu conseguir sair ganhando bastante experiência, um pouco como funciona os parâmetros, aprendi um pouco mais como funciona os IF, ELSIF e ELSE, obtive mais experiência sobre SELECT, entendi a funcionalidade do comando INTO, e aprendi sobre as funções de agregação.

Por mais que eu tenha perdido por um lado, eu ganhei no outro, estou tendo cada vez mais confiança para usar os comando para criar os meus projeto, por eu não ter certeza do que eu estava usando e fazendo, eu me sentia meio inseguro do por que eu estava usando os comando, já que eu não estou 100% ciente de como eles funcionam de forma aprofundada.
