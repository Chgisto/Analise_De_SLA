import os
import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv



load_dotenv()

host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")

conexao = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
iniciar_conexao = create_engine(conexao)

query = "SELECT * FROM pedidos"
print("Executando a consulta SQL...")

df = pd.read_sql(query, iniciar_conexao)
print("Consulta SQL executada com sucesso!")

df_grupoby = df.groupby (['regiao', 'sla']).agg(qtd= ('sla', 'count')).reset_index()
df_grupoby['pct_regiao'] = df_grupoby.groupby('regiao')['qtd'].transform(lambda x: x / x.sum() * 100)
print(df_grupoby)

df_grupoby.to_excel('pedidos.xlsx', sheet_name = 'Pedidos sla', na_rep = 'N/A', header=True, index = False)

