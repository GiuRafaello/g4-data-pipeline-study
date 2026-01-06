import gspread
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

# ========= CARREGAR ENV =========
load_dotenv()

# ========= GOOGLE SHEETS (FORMS) =========
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = "ga4_key.json"
SPREADSHEET_NAME = "respostas_google_forms"

creds = Credentials.from_service_account_file(
    CREDS_FILE,
    scopes=SCOPES
)

client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).sheet1
data = sheet.get_all_records()

df = pd.DataFrame(data)

print("📊 Dados vindos do Google Forms:")
print(df)

# ========= POSTGRES (SUPABASE) =========
conn = psycopg2.connect(
    host=os.getenv("SUPABASE_DB_HOST"),
    database=os.getenv("SUPABASE_DB_NAME"),
    user=os.getenv("SUPABASE_DB_USER"),
    password=os.getenv("SUPABASE_DB_PASSWORD"),
    port=int(os.getenv("SUPABASE_DB_PORT"))
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO forms_responses
        (response_date, origem, canal, valor, source)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["Carimbo de data/hora"],
            row["Origem"],
            row["Canal"],
            row["Valor"],
            "google_forms"
        )
    )

conn.commit()
cur.close()
conn.close()

print("✅ Dados do Google Forms enviados para o Supabase com sucesso")


