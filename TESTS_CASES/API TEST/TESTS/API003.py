import pytest
import requests
from requests.exceptions import HTTPError

# Base URL para crear producto
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

# Token válido con permisos de escritura
TOKEN = "ixyz2f8u6d61isce3fhq7xqr9uozd3d"  # ⚠️ No usar este token real en documentación pública

# Headers requeridos
headers = {
    "X-Auth-Token": TOKEN,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Payload para crear producto
payload = {
    "name": "PyTest Widget 3000",
    "type": "physical",
    "price": 19.99,
    "weight": 0.5,
    "categories": [23]  # Cambiar por un ID de categoría válido en tu tienda
}

def test_add_new_product_valid_payload():
    try:
        # Enviar POST para crear el producto
        response = requests.post(BASE_URL, headers=headers, json=payload)

        # Validar código de estado
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        # Validar que la respuesta contiene 'data' y campos esperados
        data = response.json()
        assert "data" in data, "'data' key not found in response"
        assert data["data"]["name"] == payload["name"], "Product name mismatch"
        assert "id" in data["data"], "Product ID not found in response"

        print(f"✅ Product created with ID: {data['data']['id']}")

    except HTTPError as http_err:
        pytest.fail(f"HTTP error occurred: {http_err}")

    except Exception as err:
        pytest.fail(f"Unexpected error: {err}")
