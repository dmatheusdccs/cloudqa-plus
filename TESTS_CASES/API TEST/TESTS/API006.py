import requests
from concurrent.futures import ThreadPoolExecutor

# Base URL para la API de productos
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

# Headers
headers = {
    "X-Auth-Token": "roztjzwshb4wh76b3jfoqvardwkm50r",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Lista de productos a crear
products = [
    {"name": "Async Product 1", "type": "physical", "sku": "AP001", "price": 20.99, "weight": 0.5, "categories": [23], "is_visible": True},
    {"name": "Async Product 2", "type": "physical", "sku": "AP002", "price": 30.50, "weight": 0.7, "categories": [23], "is_visible": True},
    {"name": "Async Product 3", "type": "physical", "sku": "AP003", "price": 45.00, "weight": 1.0, "categories": [23], "is_visible": True},
    {"name": "Async Product 4", "type": "physical", "sku": "AP004", "price": 15.75, "weight": 0.3, "categories": [23], "is_visible": True}
]

# Función para crear un producto
def create_product(product):
    response = requests.post(BASE_URL, headers=headers, json=product)
    return f"SKU: {product['sku']} - Status: {response.status_code}"

# Usando ThreadPoolExecutor para enviar requests en paralelo
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(create_product, products)

# Mostrar resultados
for result in results:
    print(result)
