import requests

BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

headers = {
    "X-Auth-Token": "roztjzwshb4wh76b3jfoqvardwkm50r",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Payload inválido (faltan campos requeridos como 'name', 'price', etc.)
invalid_payload = {
    "type": "physical"
}

response = requests.post(BASE_URL, headers=headers, json=invalid_payload)

print(f"Status Code: {response.status_code}")
print("Response Body:")
print(response.text)
