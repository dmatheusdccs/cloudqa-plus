import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_access_inventory_after_logout(browser):
    page = browser.new_page()
    
    # Login válido
    page.goto('https://www.saucedemo.com/')
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')
    page.wait_for_selector(".shopping_cart_link", timeout=5000)
    
    # Hacer logout
    page.click('#react-burger-menu-btn')  # Abrir menú
    page.wait_for_selector('#logout_sidebar_link')
    page.click('#logout_sidebar_link')
    
    # Intentar navegar a inventario después del logout
    page.goto('https://www.saucedemo.com/inventory.html')
    
    # Validar que la URL sea la página de inventario (esto debería fallar porque el usuario debe ser redirigido al login)
    assert page.url == 'https://www.saucedemo.com/', "User should NOT access inventory page after logout"
    
    page.close()
