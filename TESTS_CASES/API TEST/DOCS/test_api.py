import requests

def test_get_product_list_with_auth():
    # URL de la API de BigCommerce
    url = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

    # Agregar el token de autenticación al encabezado
    headers = {
        "X-Auth-Token": "ixyz2f8u6d61isce3fhq7xqr9uozd3d"  # Reemplaza con tu token real
    }

    # Hacer la solicitud GET con el token de autenticación
    response = requests.get(url, headers=headers)

    # Verificar el código de estado de la respuesta (debería ser 200 si el token es válido)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Verificar que la respuesta contiene productos (opcional, depende de la respuesta de la API)
    assert "data" in response.json(), "Expected 'data' in response, no data found."
    
    # Imprimir la respuesta para verificar
    print(response.json())  # Opcional, solo para ver los productos
