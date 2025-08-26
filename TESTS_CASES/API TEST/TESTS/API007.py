import requests

# Base URL
BASE_URL = "https://api.bigcommerce.com/stores/hp1ltb9vhs/v3/catalog/products"

# Headers
headers = {
    "X-Auth-Token": "roztjzwshb4wh76b3jfoqvardwkm50r",
    "Accept": "application/json"
}

# Parámetros de filtros y paginación
params = {
    "price:min": 20,           # Precio mínimo
    "categories:in": "23",     # ID de categoría
    "is_visible": True,        # Solo productos visibles
    "limit": 2,                # Productos por página
    "page": 1                  # Página inicial
}

all_products = []
while True:
    response = requests.get(BASE_URL, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        print("Error:", response.text)
        break

    data = response.json()
    products = data.get("data", [])
    if not products:
        break

    # Guardar productos
    all_products.extend(products)

    # Si no hay más páginas, salir
    meta = data.get("meta", {})
    pagination = meta.get("pagination", {})
    if params["page"] >= pagination.get("total_pages", 1):
        break

    # Siguiente página
    params["page"] += 1

# Mostrar resultados
for p in all_products:
    print(f"ID: {p['id']} | Name: {p['name']} | Price: {p['price']}")
