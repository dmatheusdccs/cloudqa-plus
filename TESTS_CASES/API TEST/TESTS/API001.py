import pytest
import requests
from requests.exceptions import HTTPError

# URL base de la API
BASE_URL = "https://api.bigcommerce.com/stores/{store_hash}/v3/products"

# Token de autenticación
BEARER_TOKEN = "YOUR_VALID_BEARER_TOKEN"  # Reemplazar con un token válido

# Headers con el token de autorización
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Accept": "application/json"
}


# Test case: Obtener lista de productos con un token válido
def test_get_product_list_valid_token():
    try:
        # Enviar solicitud GET a la API
        response = requests.get(BASE_URL, headers=headers)

        # Validar que la respuesta sea exitosa
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Validar que la respuesta contenga campos como 'id', 'name', 'price'
        data = response.json()
        assert isinstance(data, list), "Response should be a list"
        for product in data:
            assert "id" in product, "Product missing 'id'"
            assert "name" in product, "Product missing 'name'"
            assert "price" in product, "Product missing 'price'"

        print("Test passed successfully!")

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        assert False, f"HTTP error: {http_err}"

    except Exception as err:
        print(f"Other error occurred: {err}")
        assert False, f"Other error: {err}"

