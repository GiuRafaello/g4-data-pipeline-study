import pandas as pd

# Caminho do arquivo Excel
file_path = "dados_excel.xlsx"

# Ler planilha
df = pd.read_excel(file_path)

print("📊 Dados vindos do Excel:")
print(df)

print("\n📐 Tipos das colunas:")
print(df.dtypes)
