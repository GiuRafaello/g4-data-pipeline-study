from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
import pandas as pd
from sqlalchemy import create_engine

# ======================
# CONFIG
# ======================
PROPERTY_ID = "517934290"

DATABASE_URL = (
    "postgresql://postgres.dfrdrbqecpdztxjmednz:"
    "giuluce2307@aws-0-us-west-2.pooler.supabase.com:5432/postgres"
)

# ======================
# CLIENT
# ======================
client = BetaAnalyticsDataClient()

request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[
        Dimension(name="eventName"),
        Dimension(name="date"),
        Dimension(name="platform"),
        Dimension(name="country"),
    ],
    metrics=[
        Metric(name="eventCount"),
    ],
    date_ranges=[
        DateRange(start_date="30daysAgo", end_date="today")
    ],
)

response = client.run_report(request)

# ======================
# DATAFRAME
# ======================
rows = []

for row in response.rows:
    rows.append({
        "event_name": row.dimension_values[0].value,
        "date": row.dimension_values[1].value,
        "platform": row.dimension_values[2].value,
        "country": row.dimension_values[3].value,
        "event_count": int(row.metric_values[0].value),
    })

df = pd.DataFrame(rows)

# ======================
# LOAD → BRONZE
# ======================
engine = create_engine(DATABASE_URL)

print("TOTAL DE LINHAS:", len(df))
print(df.head())

df.to_sql(
    "ga4_events_bronze",
    engine,
    if_exists="append",
    index=False,
    schema="public"
)

print("OK - GA4 BRONZE CARREGADO")



