import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Caminho da chave
KEY_PATH = "ga4_key.json"

# Escopos necessários
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Autenticação
credentials = Credentials.from_service_account_file(
    KEY_PATH,
    scopes=scopes
)

client = gspread.authorize(credentials)

# 🔴 IMPORTANTE: nome da planilha
SPREADSHEET_ID = "1QDrRpTNGNlsLnWLpS72h0T_UYfU_eyDeznDs0HV32DY"

sheet = client.open_by_key(SPREADSHEET_ID).sheet1


# Ler dados
data = sheet.get_all_records()
df = pd.DataFrame(data)

print("📊 Dados vindos do Google Forms:")
print(df)
