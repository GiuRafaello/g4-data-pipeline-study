import pandas as pd
from pathlib import Path

# Caminho absoluto do CSV
CSV_PATH = Path(
    r"C:\Users\giu_r\OneDrive\Área de Trabalho\G4\dbt_g4\dados_excel.csv"
)

# Leitura correta do CSV (separador brasileiro)
df = pd.read_csv(
    CSV_PATH,
    sep=";",
    encoding="utf-8"
)

# Padroniza nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Converte a coluna de data manualmente (forma correta)
df["data_evento"] = pd.to_datetime(
    df["data_evento"],
    dayfirst=True,
    errors="raise"
)

# (Opcional) Garantir tipo numérico
df["valor"] = pd.to_numeric(df["valor"], errors="raise")

# Log simples para conferência
print("Arquivo lido com sucesso")
print(df.head())
print(df.dtypes)


