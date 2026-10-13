	
tabela 
INSERT INTO pedidos (pedidos, regiao, sla, dias) VALUES
(101, 'Sul', 'No prazo', 2),
(102, 'Sul', 'No prazo', 3),
(103, 'Sul', 'Atrasado', 5),
(104, 'Sudeste', 'No prazo', 1),
(105, 'Sudeste', 'No prazo', 2),
(106, 'Sudeste', 'No prazo', 3),
(107, 'Sudeste', 'Atrasado', 4),
(108, 'Norte', 'Atrasado', 5),
(109, 'Norte', 'Atrasado', 6),
(110, 'Norte', 'Atrasado', 4),
(111, 'Norte', 'No prazo', 3),
(112, 'Nordeste', 'No prazo', 3),
(113, 'Nordeste', 'Atrasado', 4),
(114, 'Nordeste', 'No prazo', 2),
(115, 'Centro-Oeste', 'No prazo', 2),
(116, 'Centro-Oeste', 'No prazo', 3);
	
persona	
	SELECT regiao,
	
		count(*) AS todos_pedidos,
		count(*) filter (where sla = 'Atrasado') AS atrasados,
		ROUND(
			(count(*) filter (where sla = 'Atrasado') * 100.0) / count(*),
			1
		)::text || '%'AS atraso_porcentagem
		
	from pedidos
	group by regiao
	order by atraso_porcentagem DESC;
