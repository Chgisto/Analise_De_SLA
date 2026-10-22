import psycopg #biblioteca que permite a conexão com o banco de dados PostgreSQL
import random 

regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']

def gerar_pedidos(num_pedidos):
    dias = random.randint(1,6)
    sla = "Atrasado" if dias > 3 else "No prazo"
    regiao = random.choice(regioes)

    return(num_pedidos, regiao, sla, dias)
lista= []
for i in range(121, 5121):
    pedido = gerar_pedidos(i)
    lista.append(pedido)
try:
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="123456",
        connect_timeout=5
    ) as conexao: 
        with conexao.cursor() as cursor:
            cursor.executemany("INSERT INTO pedidos VALUES (%s, %s, %s, %s)", lista )

except psycopg.OperationalError as erro:
    print("\nNão foi possível conectar ao PostgreSQL.")
    print(f"Detalhes: {erro}") 