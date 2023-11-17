--bom o que era necessaro para aprender ja foi aprendido, agora podemos da
--continuidade, e o melhor conteudo para termos aprendido foi o NEW. agora
--podemos por em pratica conteudo como o ordenação
--
--
--

CREATE OR REPLACE FUNCTION new_id() RETURNS TRIGGER AS $$
DECLARE
   ultimo_id INT;

BEGIN
    SELECT MAX(id_compra) INTO ultimo_id FROM compras;

	NEW.id_compra := ultimo_id + 1;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER atribuindo_id_novo_registro
BEFORE INSERT
ON compras
FOR EACH ROW
EXECUTE FUNCTION new_id();

SELECT * FROM compras ORDER BY valor_pago DESC;