import pytest
import requests


# URL base de la API
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

# Test case: Obtener lista de productos SIN token de autenticación
def test_get_product_list_no_auth():
    try:
        # Hacer la solicitud GET sin token
        response = requests.get(BASE_URL)

        # Validar que la respuesta sea 401 Unauthorized
        assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"

        # Verificar mensaje de error en la respuesta
        assert "X-Auth-Token header is required" in response.text, f"Expected 'X-Auth-Token header is required', got {response.text}"

        print("Test passed: Unauthorized request correctly blocked.")

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        assert False, f"HTTP error: {http_err}"

    except Exception as err:
        print(f"Other error occurred: {err}")
        assert False, f"Other error: {err}"


