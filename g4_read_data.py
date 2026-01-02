from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2 import service_account

KEY_PATH = "ga4_key.json"
PROPERTY_ID = "517934290"  # só números

credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=["https://www.googleapis.com/auth/analytics.readonly"]
)

client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[
        Dimension(name="eventName")
    ],
    metrics=[
        Metric(name="eventCount")
    ],
    date_ranges=[
        DateRange(start_date="7daysAgo", end_date="today")
    ]
)

response = client.run_report(request)

print("📊 Eventos encontrados no GA4:")
for row in response.rows:
    print(
        row.dimension_values[0].value,
        row.metric_values[0].value
    )

