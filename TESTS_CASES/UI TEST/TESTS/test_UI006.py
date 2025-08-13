import pytest
from playwright.sync_api import sync_playwright

# Fixture para iniciar y cerrar el navegador
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Modo visible para ver el fallo
        yield browser
        browser.close()

# Prueba para agregar un producto inexistente al carrito
@pytest.mark.xfail  # Esto marca la prueba como "Expected Failure"
def test_add_nonexistent_product(browser):
    page = browser.new_page()
    
    # 1. Abrir la página de login
    page.goto('https://www.saucedemo.com/')
    
    # 2. Ingresar credenciales válidas
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')
    
    # 3. Esperar que la página de inventario esté cargada
    page.wait_for_selector(".inventory_list", timeout=5000)
    
    # 4. Intentar hacer clic en un botón inexistente
    try:
        page.wait_for_selector('button[id="add-to-cart-nonexistent-product"]', timeout=3000)
        page.click('button[id="add-to-cart-nonexistent-product"]')
    except Exception as e:
        page.screenshot(path="UI006_add_nonexistent_product_error.png")
        raise e  # Forzar que la prueba falle
    
    # 5. Cerrar la página
    page.close()
