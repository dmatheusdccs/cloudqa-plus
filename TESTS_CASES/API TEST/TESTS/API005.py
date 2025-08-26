import requests

# Endpoint para eliminar producto
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products/99999"

headers = {
    "X-Auth-Token": "roztjzwshb4wh76b3jfoqvardwkm50r",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.delete(BASE_URL, headers=headers)

print(f"Status Code: {response.status_code}")
print("Response Body:")
print(response.text if response.text else "<No Content>")
