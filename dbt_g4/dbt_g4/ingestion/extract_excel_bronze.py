import pandas as pd
from sqlalchemy import create_engine, text

# ======================
# CONFIG
# ======================
CSV_PATH = r"C:\Users\giu_r\OneDrive\Área de Trabalho\G4\dbt_g4\dados_excel.csv"

DATABASE_URL = (
    "postgresql://postgres.dfrdrbqecpdztxjmednz:"
    "giuluce2307@aws-0-us-west-2.pooler.supabase.com:5432/postgres"
)

# ======================
# EXTRACT
# ======================
df = pd.read_csv(
    CSV_PATH,
    sep=",",
    parse_dates=["data_evento"],
    dayfirst=True
)

# Padroniza nomes das colunas
df.columns = df.columns.str.lower()

print("TOTAL DE LINHAS:", len(df))
print(df.head())

# ======================
# LOAD → BRONZE
# ======================
engine = create_engine(DATABASE_URL)

with engine.begin() as conn:
    # Limpa tabela bronze
    conn.execute(text("truncate table public.g4_excel_bronze;"))

    # Insere dados
    df.to_sql(
        "g4_excel_bronze",
        conn,
        schema="public",
        if_exists="append",
        index=False
    )

print("✅ OK - EXCEL BRONZE CARREGADO")

