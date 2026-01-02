import requests
import uuid

MEASUREMENT_ID = "G-X9KZJPY9NX"
API_SECRET = "EeBhMHRzQZWcAKhRny7J1w"

url = (
    "https://www.google-analytics.com/mp/collect"
    f"?measurement_id={MEASUREMENT_ID}&api_secret={API_SECRET}"
)

payload = {
    "client_id": str(uuid.uuid4()),
    "events": [
        {
            "name": "teste_pipeline",
            "params": {
                "origem": "python",
                "canal": "estudo",
                "valor": 42
            }
        }
    ]
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Resposta:", response.text)
