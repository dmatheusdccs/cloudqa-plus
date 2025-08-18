import pytest
import requests
from requests.exceptions import HTTPError

# URL base de la API
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

# Token de autenticación
BEARER_TOKEN = "123456789xxxxxxxxxx"  # Reemplazar con tu token válido

# Headers
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Payload inválido (faltan campos obligatorios como name y price)
invalid_payload = {
    "type": "physical",
    "weight": 1.0
}

def test_add_product_invalid_payload():
    try:
        # Enviar POST con payload inválido
        response = requests.post(BASE_URL, headers=headers, json=invalid_payload)

        # Validar que devuelve 400 Bad Request
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"

        # Validar que en el mensaje se menciona el error
        error_text = response.text.lower()
        assert "error" in error_text or "invalid" in error_text, "No error message found in response"

        print("✅ API correctly returned 400 Bad Request for invalid payload.")

    except HTTPError as http_err:
        pytest.fail(f"HTTP error occurred: {http_err}")

    except Exception as err:
        pytest.fail(f"Unexpected error: {err}")
