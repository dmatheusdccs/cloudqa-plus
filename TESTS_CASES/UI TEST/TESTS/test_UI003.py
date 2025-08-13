import pytest
from playwright.sync_api import sync_playwright

# Fixture para iniciar y cerrar el navegador
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Puedes cambiar a firefox o webkit si quieres
        yield browser
        browser.close()

# Prueba de navegación al carrito de compras
def test_navigate_to_shopping_cart(browser):
    page = browser.new_page()
    
    # 1. Abrir la página de login
    page.goto('https://www.saucedemo.com/')
    
    # 2. Ingresar credenciales válidas
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')

    # 3. Esperar hasta que cargue la página principal
    page.wait_for_selector(".shopping_cart_link", timeout=5000)

    # 4. Hacer clic en el ícono del carrito
    page.click(".shopping_cart_link")

    # 5. Verificar que se redirige a la página del carrito
    try:
        page.wait_for_url("https://www.saucedemo.com/cart.html", timeout=5000)
        assert page.url == "https://www.saucedemo.com/cart.html"
        print("Navigation to shopping cart successful.")
    except Exception as e:
        page.screenshot(path="navigate_cart_error.png")
        raise e

    page.close()
