import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ======================
# CONFIG
# ======================

CSV_PATH = Path(
    r"C:\Users\giu_r\OneDrive\Área de Trabalho\G4\dbt_g4\dados_excel.csv"
)

DATABASE_URL = (
    "postgresql://postgres.dfrdrbqecpdztxjmednz:"
    "giuluce2307@aws-0-us-west-2.pooler.supabase.com:5432/postgres"
)

TABLE_NAME = "excel_events_bronze"
SCHEMA = "public"

# ======================
# EXTRACT
# ======================

df = pd.read_csv(
    CSV_PATH,
    sep=";",
    encoding="utf-8"
)

# Padronização de colunas
df.columns = df.columns.str.strip().str.lower()

# Conversões de tipo
df["data_evento"] = pd.to_datetime(
    df["data_evento"],
    dayfirst=True,
    errors="raise"
)

df["valor"] = pd.to_numeric(df["valor"], errors="raise")

# ======================
# LOG DE VALIDAÇÃO
# ======================

print("Arquivo lido com sucesso")
print("Total de linhas:", len(df))
print(df.head())
print(df.dtypes)

# ======================
# LOAD → BRONZE
# ======================

engine = create_engine(DATABASE_URL)

df.to_sql(
    TABLE_NAME,
    engine,
    if_exists="replace",   # mesmo padrão usado no GA4
    index=False,
    schema=SCHEMA
)

print("OK - EXCEL BRONZE CARREGADO COM SUCESSO")



