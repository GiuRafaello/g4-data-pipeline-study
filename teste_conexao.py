import psycopg2

print("TESTE CONEXÃO")

conn = psycopg2.connect(
    host="aws-1-us-east-1.pooler.supabase.com",
    dbname="postgres",
    user="postgres",
    password="lucejuan2307!",
    port=6543,
    sslmode="require"
)

print("CONECTOU COM SUCESSO")
conn.close()
