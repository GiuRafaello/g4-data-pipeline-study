import gspread
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

print("INICIO DO SCRIPT")

load_dotenv()
print("ENV CARREGADO")

# ========= GOOGLE SHEETS =========
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = "ga4_key.json"
SPREADSHEET_NAME = "respostas_google_forms"

creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
print("CONECTOU NO GOOGLE")

sheet = client.open(SPREADSHEET_NAME).sheet1
data = sheet.get_all_records()

df = pd.DataFrame(data)
df.columns = df.columns.str.strip()

print("DATAFRAME CRIADO")
print(df)

print("ANTES DO POSTGRES")

# ========= POSTGRES =========
import psycopg2

import os

conn = psycopg2.connect( 
    host=os.getenv("SUPABASE_DB_HOST"),
    port=os.getenv("SUPABASE_DB_PORT"), 
    database=os.getenv("SUPABASE_DB_NAME"), 
    user=os.getenv("SUPABASE_DB_USER"), 
    password=os.getenv("SUPABASE_DB_PASSWORD") )


print("CONECTOU NO POSTGRES")

cur = conn.cursor()

print("CONECTOU NO POSTGRES")

cur = conn.cursor()

for _, row in df.iterrows():
    print("INSERINDO:", row["Origem"])

    cur.execute(
        """
        INSERT INTO forms_responses
        (response_date, origem, canal, valor, source)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            pd.to_datetime(row["Carimbo de data/hora"], dayfirst=True),
            row["Origem"],
            row["Canal"],
            int(row["Valor"]),
            "google_forms"
        )
    )

conn.commit()
print("COMMIT FEITO")

cur.close()
conn.close()

print("FIM DO SCRIPT")

